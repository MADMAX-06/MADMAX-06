from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://volgograd.t2.ru/"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

def test_first_tarif():
    element = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/section/section/div/div/div/div[1]/a/div/div[1]/div[1]/h3")
    x = element.text
    test_passed = "ХВАТИТ!"
    assert test_passed == x, f"Ожидаемый результат {test_passed}, Фактический результат: {x}"

def test_second_tarif:
    pass
def test_fhird_tarif:
    pass

if __name__ == "__main__":
    test_basket()
    print("Тест пройден")