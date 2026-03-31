from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_15():
    """
    Dummy test run for scenario 15
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_15")

    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_827")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_626")
    assert "Dashboard" in driver.title
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_837")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_762")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_412")

    driver.quit()

if __name__ == "__main__":
    execute_test_15()
