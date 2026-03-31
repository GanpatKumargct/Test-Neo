from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_1():
    """
    Dummy test run for scenario 1
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_1")

    driver.find_element(By.ID, "user_name").send_keys("test_data_586")
    assert "Dashboard" in driver.title
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_897")
    time.sleep(2)
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert "Dashboard" in driver.title
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_871")
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_894")

    driver.quit()

if __name__ == "__main__":
    execute_test_1()
