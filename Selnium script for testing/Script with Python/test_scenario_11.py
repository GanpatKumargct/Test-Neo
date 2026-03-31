from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_11():
    """
    Dummy test run for scenario 11
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_11")

    driver.find_element(By.ID, "user_name").send_keys("test_data_442")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "password_field").send_keys("test_data_107")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_889")
    driver.find_element(By.ID, "user_name").send_keys("test_data_500")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_853")

    driver.quit()

if __name__ == "__main__":
    execute_test_11()
