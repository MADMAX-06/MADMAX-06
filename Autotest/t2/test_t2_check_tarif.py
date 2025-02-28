from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestCheckTarif(unittest.TestCase):
    def setUp(self):
        self.link = "https://volgograd.t2.ru/"
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_check_tarif_hvatit(self):
        test_passed = "ХВАТИТ!"
        self.browser.get(self.link)
        element = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/section/section/div/div/div/div[1]/a/div/div[1]/div[1]/h3")
        