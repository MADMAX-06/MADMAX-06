from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.tbank.ru/"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
find_button = browser.find_element(By.CLASS_NAME, "abf1aN3J0")
find_button.click()
time.sleep(2)

find_card = browser.find_element(By.CSS_SELECTOR, "div.cbw68J0RB[data-qa-type='uikit/individualDesign.preview']:nth-child(3)")
find_card.click()

'''find_spisok = browser.find_element(By.CLASS_NAME, "KbJtn8Ajg")
find_spisok.click()'''
time.sleep(1)
find_fio = browser.find_element(By.CSS_SELECTOR, "input[name='fio']")
find_fio.send_keys("Тестов Тест Тестович")
time.sleep(1)
find_phone_mobile = browser.find_element(By.CSS_SELECTOR, "input[name='phone_mobile']")
find_phone_mobile.send_keys("3333333333")
time.sleep(1)
find_email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
find_email.send_keys("test@test.ru")
time.sleep(1)

find_birthdate = browser.find_element(By.CSS_SELECTOR, "input[name='birthdate']")
find_birthdate.send_keys("01012011")

time.sleep(20)


