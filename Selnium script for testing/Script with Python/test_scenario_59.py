from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_59():
    """
    Dummy test run for scenario 59
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_59")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_912")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_397")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_327")
    driver.find_element(By.ID, "checkout_btn").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_306")
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_59()
