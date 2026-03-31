from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_58():
    """
    Dummy test run for scenario 58
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_58")

    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_701")
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_395")
    driver.find_element(By.ID, "user_name").send_keys("test_data_927")
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_58()
