from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


link = "https://volgograd.hh.ru/"
browser = webdriver.Chrome(options=options)
browser.get(link)

vacancy = "Тестировщик"

find_input = browser.find_element(By.ID, "a11y-search-input")
find_input.send_keys(vacancy)
find_input.send_keys(Keys.ENTER)
modal_button = browser.find_element(By.CSS_SELECTOR, "div.bloko-modal-close-button")
modal_button.click()

time.sleep(5)

find_result_vacancy = browser.find_element(By.ID, "a11y-main-content")
result_vacancy = find_result_vacancy.text

def test_result_vacancy():
    assert vacancy in result_vacancy, f"Ожидаемый результат. Фактичсеский результат."

if __name__ == "__main__":
    test_result_vacancy()
    print("Тест пройден")

