from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_35():
    """
    Dummy test run for scenario 35
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_35")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_35()
