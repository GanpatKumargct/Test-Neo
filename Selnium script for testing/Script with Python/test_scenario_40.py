from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_40():
    """
    Dummy test run for scenario 40
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_40")

    driver.find_element(By.NAME, "password_field").send_keys("test_data_509")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_697")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_918")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_103")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_40()
