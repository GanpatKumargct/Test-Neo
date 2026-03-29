import os
import sys

# Add current directory to path so we can import app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

from app.services.llm_parser import LLMParser
import traceback

def test():
    parser = LLMParser()
    try:
        res = parser.parse("driver.get('http://google.com')\ndriver.find_element(By.ID, 'q').send_keys('test')")
        print("SUCCESS:", res)
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    test()
