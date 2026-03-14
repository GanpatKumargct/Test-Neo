"""
Parse Python source with AST to extract Selenium-related steps.
Produces a list of step dicts suitable for TestNeo conversion.
"""

import ast
from typing import Any


from .base_parser import BaseParser

# Selenium method names we care about
FIND_NAMES = ("find_element", "find_elements", "find_element_by_id", "find_element_by_xpath", "find_element_by_link_text", "find_element_by_partial_link_text", "find_element_by_name", "find_element_by_tag_name", "find_element_by_class_name", "find_element_by_css_selector")
ACTIONS = ("click", "send_keys", "clear", "get_attribute", "submit", "close", "quit")


class PythonParser(BaseParser):
    def _get_constant_value(self, node: ast.expr) -> Any:
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
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            # For enumerations like Keys.ENTER
            return f"{node.value.id}.{node.attr}"
        return None
        return None

    def _get_selector_from_call(self, call: ast.Call) -> tuple[str, str] | None:
        """From driver.find_element(By.XXX, "value") return (by, value)."""
        if not isinstance(call.func, ast.Attribute):
            return None
        # Handle driver.find_element(...).click() where call is the click()
        if call.func.attr in ACTIONS and isinstance(call.func.value, ast.Call):
            call = call.func.value
            if not isinstance(call.func, ast.Attribute):
                 return None
            
        if call.func.attr not in FIND_NAMES:
            return None
            
        # Legacy extract
        if call.func.attr.startswith("find_element_by_"):
            by = call.func.attr.replace("find_element_by_", "")
            if len(call.args) > 0:
                val = self._get_constant_value(call.args[0])
                return by, val if val is not None else ""
            return by, ""
            
        if len(call.args) < 2:
            return None
        by_node, value_node = call.args[0], call.args[1]
        if isinstance(by_node, ast.Call) and isinstance(by_node.func, ast.Attribute):
            if getattr(by_node.func.value, "id", None) == "By":
                by = by_node.func.attr.lower()
                val = self._get_constant_value(value_node)
                return by, val if val is not None else ""
        elif isinstance(by_node, ast.Attribute):
            if getattr(by_node.value, "id", None) == "By":
                by = by_node.attr.lower()
                val = self._get_constant_value(value_node)
                return by, val if val is not None else ""
        return None

    def parse(self, source: str) -> list[dict[str, Any]]:
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
                    # driver = Chrome() / webdriver.Chrome()
                    if isinstance(node.value.func, ast.Name):
                        if node.value.func.id in ("Chrome", "Firefox", "Edge", "Safari", "Ie"):
                            steps.append({"action": "launch_browser", "browser": node.value.func.id})
                            return
                    elif isinstance(node.value.func, ast.Attribute) and getattr(node.value.func.value, "id", None) == "webdriver":
                         if node.value.func.attr in ("Chrome", "Firefox", "Edge", "Safari", "Ie"):
                             steps.append({"action": "launch_browser", "browser": node.value.func.attr})
                             return

                    # iframe = wait.until(EC.presence_of_element_located(...))
                    if isinstance(node.value.func, ast.Attribute) and node.value.func.attr == "until":
                        until_call = node.value
                        if until_call.args and isinstance(until_call.args[0], ast.Call) and isinstance(until_call.args[0].func, ast.Attribute):
                            ec_call = until_call.args[0]
                            ec_attr = ec_call.func.attr
                            if ec_attr in ("presence_of_element_located", "element_to_be_clickable"):
                                if ec_call.args and isinstance(ec_call.args[0], ast.Tuple) and len(ec_call.args[0].elts) == 2:
                                    by_node, value_node = ec_call.args[0].elts[0], ec_call.args[0].elts[1]
                                    by = by_node.attr.lower() if isinstance(by_node, ast.Attribute) else None
                                    val = self._get_constant_value(value_node)
                                    if ec_attr == "presence_of_element_located":
                                        steps.append({"action": "wait_presence", "by": by, "value": val})
                                    elif ec_attr == "element_to_be_clickable":
                                        steps.append({"action": "wait_clickable", "by": by, "value": val})
                                    # store the selector for the returned variable
                                    if by and val is not None:
                                        var_to_selector[target_name] = (by, val)
                        return

                    s = self._get_selector_from_call(node.value)
                    if s:
                        var_to_selector[target_name] = s
                return
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call = node.value
                if not isinstance(call.func, ast.Attribute):
                    return
                attr = call.func.attr
                
                # time.sleep(x)
                if attr == "sleep" and isinstance(call.func.value, ast.Name) and call.func.value.id == "time":
                    val = self._get_constant_value(call.args[0]) if call.args else None
                    if val is not None:
                        steps.append({"action": "sleep", "value": val})
                    return

                # driver.switch_to.frame(iframe)
                if attr == "frame" and isinstance(call.func.value, ast.Attribute) and call.func.value.attr == "switch_to":
                    val = self._get_constant_value(call.args[0]) if call.args else None
                    if val is None and call.args and isinstance(call.args[0], ast.Name):
                        # Use the variable name if we can't get the literal
                        val = call.args[0].id
                    if val is not None:
                        steps.append({"action": "switch_frame", "value": str(val)})
                    return

                # driver.get(url)
                if attr == "get":
                    url = self._get_constant_value(call.args[0]) if call.args else None
                    if url is not None:
                        steps.append({"action": "get", "url": str(url)})
                    return
                
                # wait.until(EC.element_to_be_clickable(...)).click()
                if attr == "click" and isinstance(call.func.value, ast.Call) and isinstance(call.func.value.func, ast.Attribute) and call.func.value.func.attr == "until":
                    until_call = call.func.value
                    if until_call.args and isinstance(until_call.args[0], ast.Call) and isinstance(until_call.args[0].func, ast.Attribute):
                        ec_call = until_call.args[0]
                        ec_attr = ec_call.func.attr # element_to_be_clickable
                        if ec_call.args and isinstance(ec_call.args[0], ast.Tuple) and len(ec_call.args[0].elts) == 2:
                            by_node, value_node = ec_call.args[0].elts[0], ec_call.args[0].elts[1]
                            by = by_node.attr.lower() if isinstance(by_node, ast.Attribute) else None
                            val = self._get_constant_value(value_node)
                            if ec_attr == "presence_of_element_located":
                                steps.append({"action": "wait_presence", "by": by, "value": val})
                            elif ec_attr == "element_to_be_clickable":
                                steps.append({"action": "wait_clickable", "by": by, "value": val})
                    # the click action is chained, so append it too
                    steps.append({"action": "click", "by": by, "value": val}) # Context is usually clear from wait
                    return
                
                # actions.move_to_element(...).send_keys(...).perform()
                if attr == "perform" and isinstance(call.func.value, ast.Call) and isinstance(call.func.value.func, ast.Attribute):
                    chained_call = call.func.value
                    if chained_call.func.attr == "send_keys":
                        send_keys_call = chained_call
                        text = self._get_constant_value(send_keys_call.args[0]) if send_keys_call.args else None
                        
                        # go up one level to see if it's move_to_element
                        if isinstance(send_keys_call.func.value, ast.Call) and isinstance(send_keys_call.func.value.func, ast.Attribute) and send_keys_call.func.value.func.attr == "move_to_element":
                            move_call = send_keys_call.func.value
                            name = move_call.args[0].id if move_call.args and isinstance(move_call.args[0], ast.Name) else None
                            by, value = None, None
                            if name and name in var_to_selector:
                                by, value = var_to_selector[name]
                            
                            steps.append({"action": "send_keys", "by": by, "value": value, "text": str(text) if text is not None else ""})
                            return

                # element.click() / element.send_keys(...) / element.clear()
                if attr in ACTIONS:
                    # check if call.func.value is a driver.find_element call directly
                    by, value = None, None
                    if isinstance(call.func.value, ast.Call):
                        s = self._get_selector_from_call(call.func.value)
                        if s:
                            by, value = s
                    
                    # resolve call.func.value (e.g. "element") to selector
                    elif isinstance(call.func.value, ast.Name):
                        name = call.func.value.id
                        if name in var_to_selector:
                            by, value = var_to_selector[name]
                    elif isinstance(call.func.value, ast.Attribute) and call.func.value.attr == "find_element":
                         # fallback for direct find_element.click() where it wasn't caught by the above rule
                         # this is necessary because call.func is the find_element.click attr and call.func.value is the driver.find_element node
                         pass
                            
                    step: dict[str, Any] = {"action": attr, "by": by, "value": value}
                    if attr == "send_keys" and call.args:
                        text = self._get_constant_value(call.args[0])
                        if text is not None:
                            step["text"] = str(text)
                    steps.append(step)
                return
            # Recurse
            for child in ast.iter_child_nodes(node):
                visit(child)

        visit(tree)

        return steps


# Legacy support
def parse_selenium_steps(source: str) -> list[dict[str, Any]]:
    return PythonParser().parse(source)
