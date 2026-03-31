from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_13():
    """
    Dummy test run for scenario 13
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_13")

    driver.find_element(By.LINK_TEXT, "Log Out").click()
    time.sleep(2)
    assert "Dashboard" in driver.title
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_388")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_256")
    time.sleep(2)
    driver.find_element(By.ID, "user_name").send_keys("test_data_176")
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_889")

    driver.quit()

if __name__ == "__main__":
    execute_test_13()
