from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_3():
    """
    Dummy test run for scenario 3
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_3")

    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "user_name").send_keys("test_data_210")
    time.sleep(2)
    driver.find_element(By.NAME, "password_field").send_keys("test_data_140")
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_572")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_3()
