from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_7():
    """
    Dummy test run for scenario 7
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_7")

    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_237")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_7()
