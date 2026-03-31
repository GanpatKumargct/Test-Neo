from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_25():
    """
    Dummy test run for scenario 25
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_25")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_696")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_460")

    driver.quit()

if __name__ == "__main__":
    execute_test_25()
