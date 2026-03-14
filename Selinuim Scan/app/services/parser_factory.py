from .base_parser import BaseParser
from .ast_parser import PythonParser
from .regex_parser import RegexParser

class ParserFactory:
    @staticmethod
    def get_parser(language: str) -> BaseParser:
        if language == "python":
            return PythonParser()
        return RegexParser(language)
