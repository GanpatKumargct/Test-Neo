import re
from typing import Any
from .base_parser import BaseParser

class RegexParser(BaseParser):
    """
    A generic parser using regex to find common Selenium patterns.
    Suitable for Java, C#, JS/TS, and Kotlin where AST parsing is complex in Python.
    """
    
    PATTERNS = {
        "get": [
            r'driver\.get\s*\(\s*["\'](.*?)["\']\s*\)',
            r'navigate\s*\(\s*\)\s*\.to\s*\(\s*["\'](.*?)["\']\s*\)'
        ],
        "find": r'find_?element[s]?\s*\(\s*(?:By\.)?(\w+)\s*,\s*["\'](.*?)["\']\s*\)',
        "click": r'\.click\s*\(\s*\)',
        "send_keys": r'\.send_?keys\s*\(\s*["\'](.*?)["\']\s*\)',
        "clear": r'\.clear\s*\(\s*\)',
    }

    def __init__(self, language: str):
        self.language = language

    def parse(self, source: str) -> list[dict[str, Any]]:
        steps = []
        var_to_selector = {}
        
        # 1. First pass: Find variable assignments
        # e.g., WebElement searchBox = driver.findElement(By.name("q"));
        # e.g., const btn = driver.findElement(By.cssSelector(".btn"));
        assign_pattern = r'(\w+)\s*=\s*.*find_?element[s]?\s*\(\s*(?:By\.)?(\w+)\s*\(?\s*["\'](.*?)["\']\s*\)?'
        for match in re.finditer(assign_pattern, source):
            var_name, by, value = match.groups()
            var_to_selector[var_name] = (by.lower(), value)

        # 2. Second pass: Find actions line by line to maintain order
        lines = source.splitlines()
        for line in lines:
            # Check for navigation
            for p in self.PATTERNS["get"]:
                match = re.search(p, line)
                if match:
                    steps.append({"action": "get", "url": match.group(1)})
            
            # Check for element actions: (var).click(), (var).sendKeys("...")
            # Pattern: (variable).(action)(...args...)
            action_pattern = r'(\w+)\.(click|send_?Keys|clear|sendKeys)\s*\((.*?)\)'
            match = re.search(action_pattern, line)
            if match:
                var_name, action, args = match.groups()
                action = "send_keys" if "send" in action.lower() else action.lower()
                
                by, val = None, None
                if var_name in var_to_selector:
                    by, val = var_to_selector[var_name]
                
                step = {"action": action, "by": by, "value": val}
                if action == "send_keys":
                    # extract text from args: "text" or 'text'
                    text_match = re.search(r'["\'](.*?)["\']', args)
                    step["text"] = text_match.group(1) if text_match else "..."
                
                steps.append(step)
            
            # Check for direct chained calls (one-liners without variables)
            # driver.findElement(...).click()
            elif "findElement" in line and (".click" in line or ".send" in line):
                find_match = re.search(self.PATTERNS["find"], line)
                if find_match:
                    by = find_match.group(1).lower()
                    val = find_match.group(2)
                    if ".click" in line:
                        steps.append({"action": "click", "by": by, "value": val})
                    elif ".send" in line:
                        keys_match = re.search(self.PATTERNS["send_keys"], line)
                        text = keys_match.group(1) if keys_match else "..."
                        steps.append({"action": "send_keys", "by": by, "value": val, "text": text})

        return steps
