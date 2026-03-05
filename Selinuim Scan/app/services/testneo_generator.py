"""Rule-based conversion of parsed Selenium steps to TestNeo format (natural language test case)."""

from typing import Any


def _step_to_nl(step: dict[str, Any]) -> str:
    """Convert a single step dict to one natural language line."""
    action = step.get("action", "")
    if action == "get":
        url = step.get("url", "")
        return f'Open URL "{url}"'
    if action == "click":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Click on element ({by}: "{val}")'
    if action == "send_keys":
        text = step.get("text", "")
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Type "{text}" into element ({by}: "{val}")'
    if action == "clear":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Clear element ({by}: "{val}")'
    if action == "get_attribute":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Get attribute from element ({by}: "{val}")'
    if action == "submit":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Submit form / element ({by}: "{val}")'
    return f"Step: {action}"


def steps_to_testneo(steps: list[dict[str, Any]], title: str = "Converted Test") -> str:
    """
    Convert a list of parsed Selenium steps to TestNeo text format.
    Output is a numbered list of natural-language steps.
    """
    lines = [f"# {title}", ""]
    for i, step in enumerate(steps, 1):
        lines.append(f"Step {i}: {_step_to_nl(step)}")
    return "\n".join(lines)


def steps_to_testneo_json(steps: list[dict[str, Any]], title: str = "Converted Test") -> dict[str, Any]:
    """Same as above but return a structured dict for API/LLM use."""
    return {
        "title": title,
        "steps": [{"index": i, "description": _step_to_nl(s), "raw": s} for i, s in enumerate(steps, 1)],
    }
