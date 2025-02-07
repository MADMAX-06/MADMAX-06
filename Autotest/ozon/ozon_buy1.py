from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
button1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div/div[2]/div/div[2]/form/button")
button1.click()
time.sleep(1)
element = driver.find_element(By.XPATH, "//*[text()='Программируем на Python | Доусон Майкл']")
element.click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jz0_27 b2121-a0 b2121-b2 b2121-a4")))
book1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[6]/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/button/div[2]")
book1.click()


time.sleep(2)
# закрываем браузер после всех манипуляций
driver.quit()