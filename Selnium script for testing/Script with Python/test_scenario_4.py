from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_4():
    """
    Dummy test run for scenario 4
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_4")

    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "user_name").send_keys("test_data_859")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_352")
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_375")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CLASS_NAME, "nav-item").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_4()
