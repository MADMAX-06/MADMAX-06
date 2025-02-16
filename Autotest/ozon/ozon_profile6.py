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
# Autotest. Пользователь использует Госуслуги для авторизации"
expected_result = "Портал государственных услуг Российской Федерации" # Ожидаемый результат

# Переходим на сайт
driver.get("https://www.ozon.ru/")

time.sleep(2)
find_profile = driver.find_element(By.CLASS_NAME, "m_47").click()

time.sleep(2)
iframe = driver.find_element(By.ID, "authFrame")
driver.switch_to.frame(iframe)

find_gosuslugi = driver.find_element(By.CSS_SELECTOR, "div[data='[object Object]']").click()
time.sleep(5)

# Получаем список всех открытых окон (вкладок)
windows = driver.window_handles

# Переключаемся на вторую вкладку
driver.switch_to.window(windows[1])

find_button = driver.find_element(By.CSS_SELECTOR, "button.plain-button").click()
time.sleep(2)

find_text_gosuslugi = driver.find_element(By.TAG_NAME, "title").text


def test_check_info_auth():
    assert find_text_gosuslugi == expected_result, f"Ожидаемый результат {expected_result}"

time.sleep(2)
driver.quit()