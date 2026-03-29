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
        # Initialize OpenAI client for Ollama
        base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        api_key = os.environ.get("OLLAMA_API_KEY", "ollama")
        self.client = OpenAI(base_url=base_url, api_key=api_key, max_retries=0)
        self.model_name = os.environ.get("OLLAMA_MODEL", "deepseek-v3.2:cloud")

    def parse(self, source: str) -> list[dict[str, Any]]:
        """
        Parse source code (any language) and return a list of Selenium step dicts.
        """
        if not self.client:
            logging.error("OpenAI client is not configured.")
            return []

        system_prompt = (
            "You are an expert software reverse engineer and tester. The user will provide you with the source code of a Selenium test script in any programming language (Python, Java, JS, C#, Ruby, Kotlin, etc.). "
            "Your task is to extract all the Selenium actions performed in the script and output them as a JSON object.\n\n"
            'The JSON object MUST contain a single key "steps", which is an array of dictionaries.\n'
            "Each dictionary must have exactly this scheme format, and NO OTHER KEYS unless specified:\n"
            '- `action` (string, required): One of: `get`, `click`, `send_keys`, `clear`, `launch_browser`, `switch_frame`, `wait_presence`, `wait_clickable`, `get_attribute`, `submit`, `close`, `quit`, `sleep`.\n'
            '- `by` (string, optional): The locator strategy used (e.g. `id`, `xpath`, `name`, `css selector`, `class name`). Keep it lowercase.\n'
            '- `value` (string, optional): The value of the locator (e.g. `//div[@id="submit"]`). Or wait time for sleep.\n'
            '- `url` (string, optional): The URL navigated to for `get` action.\n'
            '- `text` (string, optional): The text typed for `send_keys` action.\n'
            '- `browser` (string, optional): The browser name for `launch_browser` action (e.g. `Chrome`, `Firefox`).\n\n'
            'Do your best to infer the `by` and `value` for clicks and waits. '
            'Return ONLY the JSON object.'
        )

        import time

        for attempt in range(3):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Extract Selenium steps from this code:\n\n{source}"}
                    ],
                    response_format={"type": "json_object"}, 
                    temperature=0.0
                )
                content = response.choices[0].message.content
                if not content:
                    return []
                data = json.loads(content)
                return data.get("steps", [])
            except openai.RateLimitError as e:
                if attempt < 2:
                    logging.warning(f"Rate limited by API. Waiting 10 seconds... (Attempt {attempt+1}/3)")
                    time.sleep(10)
                else:
                    logging.error(f"Rate limit exhausted after 3 attempts: {e}")
                    return []
            except Exception as e:
                logging.error(f"LLM Parsing failed: {e}")
                return []
        return []
