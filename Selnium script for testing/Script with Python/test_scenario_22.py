from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_22():
    """
    Dummy test run for scenario 22
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_22")

    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_382")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    execute_test_22()
