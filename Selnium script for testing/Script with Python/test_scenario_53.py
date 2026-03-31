from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_53():
    """
    Dummy test run for scenario 53
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_53")

    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_829")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_687")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_939")
    assert "Dashboard" in driver.title
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_796")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()

    driver.quit()

if __name__ == "__main__":
    execute_test_53()
