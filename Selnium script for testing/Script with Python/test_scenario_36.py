from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_36():
    """
    Dummy test run for scenario 36
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_36")

    driver.find_element(By.NAME, "password_field").send_keys("test_data_792")
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_36()
