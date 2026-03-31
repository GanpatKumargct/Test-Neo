import json
from app.services.llm_parser import LLMParser

code = """
from selenium import webdriver
driver = webdriver.Chrome()
driver.find_element_by_id("login-button").click()
driver.find_element_by_xpath("//input[@name='user']").send_keys("test")
driver.quit()
"""
steps = LLMParser().parse(code)
print(steps)
