from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_37():
    """
    Dummy test run for scenario 37
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_37")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_494")
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_853")
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_37()
