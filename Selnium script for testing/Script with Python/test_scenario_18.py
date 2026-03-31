from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_18():
    """
    Dummy test run for scenario 18
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_18")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.ID, "user_name").send_keys("test_data_107")
    driver.find_element(By.ID, "user_name").send_keys("test_data_193")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_861")
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    driver.find_element(By.NAME, "password_field").send_keys("test_data_355")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_359")
    driver.find_element(By.CSS_SELECTOR, ".promo-code").send_keys("test_data_857")
    driver.find_element(By.NAME, "password_field").send_keys("test_data_603")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    execute_test_18()
