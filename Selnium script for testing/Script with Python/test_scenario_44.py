from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_44():
    """
    Dummy test run for scenario 44
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_44")

    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_990")
    time.sleep(2)
    driver.find_element(By.NAME, "password_field").send_keys("test_data_376")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_385")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "checkout_btn").click()
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.ID, "checkout_btn").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_44()
