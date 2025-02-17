import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Autotest. Пользователь использует конфигуратор для сборки ПК


link = "https://www.citilink.ru/"

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(link)


find_button = driver.find_element(By.CSS_SELECTOR, "a[href='/configurator/']")
find_button.click()

find_button_2 = driver.find_element(By.CSS_SELECTOR, "div[data-url='https://www.citilink.ru/configurator/add/']").click()

time.sleep(10)
