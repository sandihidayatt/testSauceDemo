import unittest
from selenium.webdriver.common.by import By

def test_success_login(driver):
    driver.get("https://www.saucedemo.com/") #buka situs
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
        