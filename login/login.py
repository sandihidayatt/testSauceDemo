import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        #steps
        driver = self.browser #buka browser
        driver.get("https://www.saucedemo.com/") #buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        #validasi
        url = driver.current_url
        self.assertIn(url,"https://www.saucedemo.com/inventory.html")
    def test_failed_login(self):
        #steps
        driver = self.browser #buka browser
        driver.get("https://www.saucedemo.com/") #buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        #validasi
        errorMessage = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn(errorMessage,"hEpic sadface: Username and password do not match any user in this service")
if __name__ == "__main__":
    unittest.main()