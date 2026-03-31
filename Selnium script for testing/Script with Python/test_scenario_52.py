from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_52():
    """
    Dummy test run for scenario 52
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_52")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_475")
    assert "Dashboard" in driver.title
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_256")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_52()
