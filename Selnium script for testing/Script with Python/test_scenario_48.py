from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_48():
    """
    Dummy test run for scenario 48
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_48")

    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    assert "Dashboard" in driver.title
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_270")
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "user_name").send_keys("test_data_548")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_645")

    driver.quit()

if __name__ == "__main__":
    execute_test_48()
