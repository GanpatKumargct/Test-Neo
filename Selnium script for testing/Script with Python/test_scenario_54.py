from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_54():
    """
    Dummy test run for scenario 54
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dummy.example.com/page_54")

    driver.find_element(By.ID, "user_name").send_keys("test_data_388")
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    driver.find_element(By.ID, "checkout_btn").click()
    assert driver.find_element(By.ID, "success_msg").is_displayed()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "nav-item").click()
    time.sleep(2)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.quit()

if __name__ == "__main__":
    execute_test_54()
