from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# Скрываем признаки использования Selenium
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Переходим на сайт
driver.get("https://www.ozon.ru/")
time.sleep(2)
input1 = driver.find_element(By.TAG_NAME, 'input')
time.sleep(1)
input1.send_keys("Книга Python")

time.sleep(1)
button1 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button1.click()
time.sleep(1)
element = driver.find_element(By.XPATH, "//*[text()='Программируем на Python | Доусон Майкл']")
element.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

get_name_of_book = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/h1")
name_of_book = get_name_of_book.text

find_price = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/span/div/div[1]/div/div")
get_price = find_price.text

time.sleep(2)
book1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div[1]/div/div/div/div[1]/button")
book1.click()

time.sleep(2)
basket = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div/div[3]/div[4]")
basket.click()

windows_2 = driver.window_handles
driver.switch_to.window(windows_2[2])

time.sleep(2)
get_name_of_book_in_basket = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div/div")
name_of_book_in_basket = get_name_of_book_in_basket.text

get_price_in_basket = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[4]/div/div[1]/div/div/span[1]")
price_in_basket = get_price_in_basket.text

#Проверяет соответствие товара в корзине
def test_check_name_of_book():
        assert name_of_book == name_of_book_in_basket, f"Ожидаемый результат: name_of_book. Фактический результат: name_of_book_in_basket"

#Проверяет соответствие цены в корзине
def test_check_price():
        assert get_price == price_in_basket, f"Ожидаемый результат: get_price. Фактический результат: price_in_basket"

time.sleep(5)
# закрываем браузер после всех манипуляций
driver.quit()