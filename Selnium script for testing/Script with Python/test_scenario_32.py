from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_32():
    """
    Dummy test run for scenario 32
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_32")

    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_162")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_391")
    time.sleep(2)
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert "Dashboard" in driver.title
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_32()
