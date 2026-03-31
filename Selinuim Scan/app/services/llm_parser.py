import json
import os
import logging
from typing import Any
from pydantic import BaseModel, Field

from openai import OpenAI
import openai
from app.core.config import settings

from .base_parser import BaseParser


class LLMParser(BaseParser):
    def __init__(self):
        # Initialize OpenAI client for Groq
        base_url = "https://api.groq.com/openai/v1"
        api_key = settings.groq_api_key
        self.client = OpenAI(base_url=base_url, api_key=api_key, max_retries=0)
        self.model_name = settings.groq_model

    def parse(self, source: str) -> str:
        """
        Parse source code (any language) and return the NLP steps as string.
        """
        if not self.client:
            logging.error("OpenAI client is not configured.")
            return []

        system_prompt = (
            "You are an expert test automation engineer.\n"
            "Task: Convert the given Selenium/Java/Python code into detailed NLP test steps.\n"
            "Strict Rules:\n"
            "1. Do NOT skip any step\n"
            "2. Expand loops into individual steps\n"
            "3. Include:\n"
            "   - clicks\n"
            "   - inputs\n"
            "   - waits\n"
            "   - conditions\n"
            "   - data extraction\n"
            "4. Keep steps in exact execution order\n"
            "5. Output only numbered steps\n"
            "6. Be explicit and human-readable"
        )

        import time

        for attempt in range(3):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Code:\n{source}"}
                    ],
                    temperature=0.0
                )
                content = response.choices[0].message.content
                if not content:
                    return ""
                return content
            except openai.RateLimitError as e:
                if attempt < 2:
                    logging.warning(f"Rate limited by API. Waiting 10 seconds... (Attempt {attempt+1}/3)")
                    time.sleep(10)
                else:
                    logging.error(f"Rate limit exhausted after 3 attempts: {e}")
                    return []
            except Exception as e:
                logging.error(f"LLM Parsing failed: {e}")
                return ""
        return ""
