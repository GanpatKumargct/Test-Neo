from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_24():
    """
    Dummy test run for scenario 24
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_24")

    driver.find_element(By.ID, "user_name").send_keys("test_data_174")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_567")
    assert "Dashboard" in driver.title
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_351")
    assert "Dashboard" in driver.title
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_754")

    driver.quit()

if __name__ == "__main__":
    execute_test_24()
