"""
Parse Python source with AST to extract Selenium-related steps.
Produces a list of step dicts suitable for TestNeo conversion.
"""

import ast
from typing import Any


# Selenium method names we care about
FIND_NAMES = ("find_element", "find_elements")
ACTIONS = ("click", "send_keys", "clear", "get_attribute", "submit")


def _get_constant_value(node: ast.expr) -> Any:
    """Extract a single constant or joined string for use as string value."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            else:
                parts.append("...")
        return "".join(parts)
    return None


def _get_selector_from_call(call: ast.Call) -> tuple[str, str] | None:
    """From driver.find_element(By.XXX, "value") return (by, value)."""
    if not isinstance(call.func, ast.Attribute):
        return None
    if call.func.attr not in FIND_NAMES:
        return None
    if len(call.args) < 2:
        return None
    by_node, value_node = call.args[0], call.args[1]
    if isinstance(by_node, ast.Call) and isinstance(by_node.func, ast.Attribute):
        if getattr(by_node.func.value, "id", None) == "By":
            by = by_node.func.attr.lower()
            val = _get_constant_value(value_node)
            return by, val if val is not None else ""
    return None


def parse_selenium_steps(source: str) -> list[dict[str, Any]]:
    """
    Parse Python source and return a list of step dicts.
    Each step: {"action": "get"|"click"|"send_keys"|"clear", "by": str|None, "value": str|None, "url"|"text": str|None}
    """
    steps: list[dict[str, Any]] = []
    # Map variable name (str) -> (by, value) for the last find_element assigned to it
    var_to_selector: dict[str, tuple[str, str]] = {}

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return steps

    def visit(node: ast.AST) -> None:
        if isinstance(node, ast.Assign):
            # target = driver.find_element(By.XX, "val")
            for t in node.targets:
                if isinstance(t, ast.Name):
                    break
            else:
                return
            target_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
            if not target_name:
                return
            if isinstance(node.value, ast.Call):
                s = _get_selector_from_call(node.value)
                if s:
                    var_to_selector[target_name] = s
            return
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if not isinstance(call.func, ast.Attribute):
                return
            attr = call.func.attr
            # driver.get(url)
            if attr == "get":
                url = _get_constant_value(call.args[0]) if call.args else None
                if url is not None:
                    steps.append({"action": "get", "url": str(url)})
                return
            # element.click() / element.send_keys(...) / element.clear()
            if attr in ACTIONS:
                # resolve call.func.value (e.g. "element") to selector
                by, value = None, None
                if isinstance(call.func.value, ast.Name):
                    name = call.func.value.id
                    if name in var_to_selector:
                        by, value = var_to_selector[name]
                step: dict[str, Any] = {"action": attr, "by": by, "value": value}
                if attr == "send_keys" and call.args:
                    text = _get_constant_value(call.args[0])
                    if text is not None:
                        step["text"] = str(text)
                steps.append(step)
            return
        # Recurse
        for child in ast.iter_child_nodes(node):
            visit(child)

    def visit_all(node: ast.AST) -> None:
        visit(node)
        for child in ast.iter_child_nodes(node):
            visit_all(child)

    visit_all(tree)

    return steps