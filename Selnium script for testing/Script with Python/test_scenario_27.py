from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_27():
    """
    Dummy test run for scenario 27
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_27")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_27()
