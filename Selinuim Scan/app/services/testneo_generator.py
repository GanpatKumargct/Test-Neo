"""Rule-based conversion of parsed Selenium steps to TestNeo format (natural language test case)."""

from typing import Any


def _step_to_nl(step: dict[str, Any]) -> str:
    """Convert a single step dict to one natural language line."""
    action = step.get("action", "")
    if action == "launch_browser":
        browser = step.get("browser", "Chrome")
        return f"Launch the {browser} browser."
    if action == "sleep":
        val = step.get("value", "a few")
        return f"Wait for {val} seconds to allow the page to load or perform further actions."
    if action == "switch_frame":
        val = step.get("value", "")
        return f"Switch the WebDriver context to the {val} iframe."
    if action == "wait_presence":
        val = step.get("value", "")
        # Try to make sense of the selector for text
        if val.startswith("iframe#"):
            val = val.replace("iframe#", "")
        return f"Wait until the {val} iframe appears on the page."
    if action == "wait_clickable":
        val = step.get("value", "")
        
        # Try to make sense of the selector for text
        clean_name = val.split('.')[-1].split('#')[-1].split('=')[-1].strip('"\']')
        if clean_name:
             return f"Wait until the {clean_name} section becomes clickable."
        return f"Wait until the element at `{val}` becomes clickable."
    if action == "get":
        url = step.get("url", "")
        return f"Navigate to the URL:\n   {url}"
    if action == "click":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        
        # General heuristics for natural language
        val_lower = val.lower()
        if "login" in val_lower or "sign-in" in val_lower or "signin" in val_lower:
            return "Click the Login button."
        if "submit" in val_lower:
            return "Click the Submit button."
        if "cookie" in val_lower or "consent" in val_lower or "privacy" in val_lower or "refuse" in val_lower or "accept" in val_lower:
            return f"Locate and click the button related to '{val.split('.')[-1]}'."
            
        # Try to extract the final name for the element
        clean_name = val.split('.')[-1].split('#')[-1].split('=')[-1].strip('"\']')
        if clean_name:
            return f"Click on the '{clean_name}' element."
            
        return f'Click on the element identified by {by}: "{val}"'
        
    if action == "send_keys":
        text = step.get("text", "")
        by = step.get("by") or "element"
        val = step.get("value") or ""
        
        # Format keys gracefully
        if text.startswith("Keys."):
            key_name = text.split('.')[-1]
            return f"Press the {key_name} key."
            
        # Try to guess the field from the selector
        val_lower = val.lower()
        field_name = "input"
        if "user" in val_lower or "email" in val_lower:
            field_name = "username/email"
        elif "pass" in val_lower:
            field_name = "password"
        elif "search" in val_lower:
            field_name = "search"
        else:
            # extract fallback name
            clean_name = val.split('.')[-1].split('#')[-1].split('=')[-1].strip('"\']')
            if clean_name:
                field_name = clean_name
            
        return f"Enter '{text}' into the {field_name} field."
        
    if action == "clear":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        
        clean_name = val.split('.')[-1].split('#')[-1].split('=')[-1].strip('"\']')
        if clean_name:
            return f"Clear the text from the '{clean_name}' field."
            
        return f'Clear the element identified by {by}: "{val}"'
    if action == "get_attribute":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Get the attribute value from the element identified by {by}: "{val}"'
    if action == "submit":
        by = step.get("by") or "element"
        val = step.get("value") or ""
        return f'Submit the form containing the element identified by {by}: "{val}"'
    if action == "close":
        return "Close the current browser tab/window."
    if action == "quit":
        return "Quit the WebDriver and close all associated browser windows."
    return f"Execute step: {action}"


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
