from .base_parser import BaseParser
from .llm_parser import LLMParser

class ParserFactory:
    @staticmethod
    def get_parser(language: str = "") -> BaseParser:
        return LLMParser()
