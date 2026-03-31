from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_41():
    """
    Dummy test run for scenario 41
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_41")

    driver.find_element(By.ID, "user_name").send_keys("test_data_174")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "user_name").send_keys("test_data_400")
    assert "Dashboard" in driver.title
    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_467")
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_41()
