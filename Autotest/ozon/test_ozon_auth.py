import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

class TestAuthorization(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Chrome()
            self.url = "https://www.ozon.ru/"
            self.user_email = "ozon_acc@yandex.ru"
            self.password = "test_password"


        def tearDown(self):
            self.driver.quit()

        def test_valid_auth(self):
            expected_info_auth = "Ваш ЛК"
            self.driver.get(self.url)
            find_profile = self.driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = self.driver.find_element(By.ID, "authFrame")
            self.driver.switch_to.frame(iframe)
            find_button_email = self.driver.find_element(By.CLASS_NAME, "lca1_47")
            find_button_email.click()
            time.sleep(2)
            email_name = self.driver.find_element(By.ID, "email")
            email_name.send_keys(self.user_email)
            time.sleep(2)
            button_auth = self.driver.find_element(By.CLASS_NAME, "b2121-a0")
            button_auth.click()
            time.sleep(1)
            info_auth = self.driver.find_element(By.CLASS_NAME, "c8012-a2")
            actual_info_auth = info_auth.text
            assert actual_info_auth == expected_info_auth, f"Ожидаемый результат {expected_info_auth}"

        def test_invalid_auth(self):
            expected_info_auth = "Заполните почту"
            self.driver.get(self.url)
            find_profile = self.driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = self.driver.find_element(By.ID, "authFrame")
            self.driver.switch_to.frame(iframe)
            find_button_email = self.driver.find_element(By.CLASS_NAME, "lca1_47")
            find_button_email.click()
            time.sleep(2)
            button_auth = self.driver.find_element(By.CLASS_NAME, "b2121-a0")
            button_auth.click()
            time.sleep(1)
            info_auth = self.driver.find_element(By.CLASS_NAME, "c8012-a2")
            actual_info_auth = info_auth.text
            assert actual_info_auth == expected_info_auth, f"Ожидаемый результат {expected_info_auth}"

        def test_gosuslugi_auth(self):
            expected_result = "Портал государственных услуг Российской Федерации"
            self.driver.get(self.url)
            find_profile = self.driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = self.driver.find_element(By.ID, "authFrame")
            self.driver.switch_to.frame(iframe)
            find_gosuslugi = driver.find_element(By.CSS_SELECTOR, "div[data='[object Object]']")
            find_gosuslugi.click()
            time.sleep(5)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            find_button = driver.find_element(By.CSS_SELECTOR, "button.plain-button")
            find_button.click()
            time.sleep(2)
            find_text_gosuslugi = driver.find_element(By.TAG_NAME, "title").text
            assert find_text_gosuslugi == expected_result, f"Ожидаемый результат {expected_result}"

        def test_invalid_number(self):
            expected_result = "Некорректный формат телефона"
            driver.get("https://www.ozon.ru/")
            time.sleep(2)
            find_profile = driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = driver.find_element(By.ID, "authFrame")
            driver.switch_to.frame(iframe)
            time.sleep(2)
            button_auth = driver.find_element(By.CLASS_NAME, "b2121-a0")
            button_auth.click()
            time.sleep(1)
            info_auth = driver.find_element(By.CLASS_NAME, "c8012-a2")
            assert info_auth.text == expected_result, f"Ожидаемый результат {expected_result}"

        def test_invalid_email(self):
            expected_result = "Некорректный формат почты"
            driver.get("https://www.ozon.ru/")
            time.sleep(2)
            find_profile = driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = driver.find_element(By.ID, "authFrame")
            driver.switch_to.frame(iframe)
            find_button_email = driver.find_element(By.CLASS_NAME, "lca1_47")
            find_button_email.click()
            time.sleep(2)
            email_name = driver.find_element(By.ID, "email")
            email_name.send_keys("d43$#@!$%^&*(%>")
            time.sleep(2)
            button_auth = driver.find_element(By.CLASS_NAME, "b2121-a0")
            button_auth.click()
            time.sleep(1)
            info_auth = driver.find_element(By.CLASS_NAME, "c8012-a2")
            assert info_auth.text == expected_result, f"Ожидаемый результат {expected_result}"

        def test_no_registration_acc(self):
            expected_result = (
                "Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона.")
            driver.get("https://www.ozon.ru/")
            time.sleep(2)
            find_profile = driver.find_element(By.CLASS_NAME, "m_47")
            find_profile.click()
            time.sleep(2)
            iframe = driver.find_element(By.ID, "authFrame")
            driver.switch_to.frame(iframe)

            find_button_email = driver.find_element(By.CLASS_NAME, "lca1_47")
            find_button_email.click()
            time.sleep(2)
            email_name = driver.find_element(By.ID, "email")
            email_name.send_keys("test@test.ru")
            time.sleep(2)
            button_auth = driver.find_element(By.CLASS_NAME, "b2121-a0")
            button_auth.click()
            time.sleep(1)
            info_auth = driver.find_element(By.CLASS_NAME, "c8012-a2")
            assert info_auth.text == expected_result, f"Ожидаемый результат {expected_result}"

if __name__ == "__main__":
    unittest.main()