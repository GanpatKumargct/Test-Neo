from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_10():
    """
    Dummy test run for scenario 10
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_10")

    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "checkout_btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_701")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_386")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_640")
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_673")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_273")
    driver.find_element(By.CLASS_NAME, "nav-item").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_10()
