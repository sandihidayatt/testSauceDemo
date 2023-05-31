import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install)

    def test_success_login(selef):
        #steps
        driver = self.browser #buka browser
        driver.get("https://wwww.saucedemo.com/") #buka situs
