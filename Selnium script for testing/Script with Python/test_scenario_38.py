from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_38():
    """
    Dummy test run for scenario 38
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_38")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "user_name").send_keys("test_data_583")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    execute_test_38()
