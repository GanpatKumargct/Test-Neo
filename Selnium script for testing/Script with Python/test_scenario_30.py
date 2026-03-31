from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_30():
    """
    Dummy test run for scenario 30
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_30")

    driver.find_element(By.CLASS_NAME, "nav-item").click()
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_919")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_581")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert "Dashboard" in driver.title

    driver.quit()

if __name__ == "__main__":
    execute_test_30()
