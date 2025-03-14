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
        languages=["ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
# Autotest. Пользователь пытается зайти на сайт не заполнив поле email, "

# Переходим на сайт
driver.get("https://www.ozon.ru/")

time.sleep(2)
find_profile = driver.find_element(By.CLASS_NAME, "m_47").click()

time.sleep(2)
iframe = driver.find_element(By.ID, "authFrame")
driver.switch_to.frame(iframe)

time.sleep(2)
button_auth = driver.find_element(By.CLASS_NAME, "b2121-a0").click()

time.sleep(1)
info_auth = driver.find_element(By.CLASS_NAME, "c8012-a2")

info_find_account = ("Заполните почту")

def test_check_info_auth():
    assert info_auth.text == info_find_account, f"Ожидаемый результат {info_find_account}"

time.sleep(2)
driver.quit()