from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_55():
    """
    Dummy test run for scenario 55
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_55")

    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Dashboard" in driver.title

    driver.quit()

if __name__ == "__main__":
    execute_test_55()
