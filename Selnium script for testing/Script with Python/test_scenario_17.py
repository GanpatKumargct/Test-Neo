from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_17():
    """
    Dummy test run for scenario 17
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_17")

    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_602")
    assert "Dashboard" in driver.title
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.NAME, "password_field").send_keys("test_data_635")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_363")
    driver.find_element(By.ID, "user_name").send_keys("test_data_763")
    time.sleep(2)
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    execute_test_17()
