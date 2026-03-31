from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_21():
    """
    Dummy test run for scenario 21
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_21")

    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_396")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_21()
