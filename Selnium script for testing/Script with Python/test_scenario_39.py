from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_39():
    """
    Dummy test run for scenario 39
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_39")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    assert "Dashboard" in driver.title
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_387")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    assert "Dashboard" in driver.title
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_243")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_39()
