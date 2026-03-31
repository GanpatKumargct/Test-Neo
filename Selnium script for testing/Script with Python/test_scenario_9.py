from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_9():
    """
    Dummy test run for scenario 9
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_9")

    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "user_name").send_keys("test_data_143")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_247")
    assert "Dashboard" in driver.title
    driver.find_element(By.NAME, "password_field").send_keys("test_data_187")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_9()
