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

