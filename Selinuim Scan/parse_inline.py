import ast
import json
from app.services.ast_parser import PythonParser

code = """
from selenium import webdriver
driver = webdriver.Chrome()
driver.find_element_by_id("login-button").click()
driver.find_element_by_xpath("//input[@name='user']").send_keys("test")
driver.quit()
"""
steps = PythonParser().parse(code)
print(json.dumps(steps, indent=2))
