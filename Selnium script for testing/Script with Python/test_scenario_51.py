from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_51():
    """
    Dummy test run for scenario 51
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_51")

    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_156")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_978")
    driver.find_element(By.CLASS_NAME, "nav-item").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_51()
