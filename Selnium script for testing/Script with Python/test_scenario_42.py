from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_42():
    """
    Dummy test run for scenario 42
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_42")

    time.sleep(2)
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()

    driver.quit()

if __name__ == "__main__":
    execute_test_42()
