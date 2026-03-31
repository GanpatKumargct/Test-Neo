from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):
    @abstractmethod
    def parse(self, source: str) -> list[dict[str, Any]] | str:
        """
        Parse source code and return a list of Selenium step dicts.
        Each step: {"action": "get"|"click"|"send_keys"|"clear", "by": str|None, "value": str|None, "url"|"text": str|None}
        """
        pass
