from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_23():
    """
    Dummy test run for scenario 23
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_23")

    driver.find_element(By.ID, "user_name").send_keys("test_data_571")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_593")
    driver.find_element(By.ID, "user_name").send_keys("test_data_416")
    driver.find_element(By.ID, "user_name").send_keys("test_data_871")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    assert "Dashboard" in driver.title
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_874")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_387")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_23()
