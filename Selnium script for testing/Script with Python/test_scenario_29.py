from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_29():
    """
    Dummy test run for scenario 29
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_29")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Dashboard" in driver.title
    assert "Dashboard" in driver.title
    assert "Dashboard" in driver.title
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_414")
    assert "Dashboard" in driver.title
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_127")

    driver.quit()

if __name__ == "__main__":
    execute_test_29()
