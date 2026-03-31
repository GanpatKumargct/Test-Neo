from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_12():
    """
    Dummy test run for scenario 12
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_12")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_152")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_253")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_542")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_429")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()

    driver.quit()

if __name__ == "__main__":
    execute_test_12()
