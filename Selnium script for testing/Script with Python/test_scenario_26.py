from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_26():
    """
    Dummy test run for scenario 26
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_26")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_124")
    time.sleep(2)
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Dashboard" in driver.title
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    assert "Dashboard" in driver.title
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_824")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_962")
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    execute_test_26()
