from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_14():
    """
    Dummy test run for scenario 14
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_14")

    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_530")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_166")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_126")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_14()
