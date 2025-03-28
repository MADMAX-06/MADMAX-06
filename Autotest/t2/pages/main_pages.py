from selenium.webdriver.common.by import By
from pages.BaseApp import BasePage
import time


class MainMenu:
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "")
    LOGIN_BUTTON = (By.XPATH, "")


class T2TarifName:
    TARIF_HVATIT = "ХВАТИТ!"
    TARIF_MY_ONLINE_PLUS = "МОЙ ОНЛАЙН+"
    TARIF_VEZDE_ONLINE = "ВЕЗДЕ ОНЛАЙН"

class T2TarifLocators:
    TARIF_HVATIT_LOCATORS = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/section/section/div/div/div/div[1]/a/div/div[1]/div[1]/h3")
    TARIF_MY_ONLINE_PLUS_LOCATORS = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/section/section/div/div/div/div[2]/a/div/div[1]/div[1]/h3")
    TARIF_VEZDE_ONLINE = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/section/section/div/div/div/div[3]/a/div/div[1]/div[1]/h3")

class SearchTarifT2(BasePage):
    def test_check_tarif_hvatit(self):
        expected_result = T2TarifName.TARIF_HVATIT
        self.driver.get(self.base_url)
        time.sleep(5)
        element = self.driver.find_element(T2TarifLocators.TARIF_HVATIT_LOCATORS)
        time.sleep(5)
        actual_info = element.text
        assert actual_info == expected_result, f"Ожидаемый результат {expected_result}"