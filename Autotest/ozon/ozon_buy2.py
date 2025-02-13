from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Автотест в процессе написания
# Проверяет, что найденный товар соответствует заданным фильтрам

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
input1.send_keys("Карта памяти")
time.sleep(1)
button1 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button1.click()
time.sleep(1)
element = driver.find_element(By.XPATH, "//span[contains(text(), 'Завтра')]")
element.click()
time.sleep(1)
element_2 = driver.find_element(By.XPATH, "//span[contains(text(), 'Kingston')]")
element_2.click()
time.sleep(1)
element_2 = driver.find_element(By.XPATH, "//span[contains(text(), 'Высокий рейтинг')]")
element_2.click()
time.sleep(1)
driver.execute_script("window. scrollBy(0, 600)")
time.sleep(1)
# Поиск двух input элементов по дочерним селекторам
inputs_in_div = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div/aside/div[2]/div[9]/div[2]/div[1]/div/div[1]/div/input')
inputs_in_div.send_keys([Keys.BACKSPACE] * 3)
inputs_in_div.send_keys("300")

inputs_in_div.send_keys(Keys.TAB)
inputs_in_div_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div/aside/div[2]/div[9]/div[2]/div[1]/div/div[2]/div/input")
inputs_in_div_2.send_keys([Keys.BACKSPACE] * 3)
inputs_in_div_2.send_keys("600")

time.sleep(5)
# закрываем браузер после всех манипуляций
driver.quit()
