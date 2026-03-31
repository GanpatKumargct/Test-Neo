from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_20():
    """
    Dummy test run for scenario 20
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_20")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_457")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_799")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_452")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_744")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_142")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_250")
    driver.find_element(By.ID, "user_name").send_keys("test_data_404")
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_20()
