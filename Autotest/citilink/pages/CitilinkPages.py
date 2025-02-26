from BaseApp import BasePage
from selenium.webdriver.common.by import By


class CitilinkSeacrhLocators:
    LOCATOR_CITILINK_SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='search']")
    LOCATOR_CITILINK_SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOCATOR_CITILINK_NAVIGATION_BAR = (By.CLASS_NAME, "div[data-meta-name='HeaderTopLinks']")
    LOCATOR_CITILINK_AUTH = (By.CSS_SELECTOR, "div[data-meta-name='UserButtonContainer']")


class SearchHelper(BasePage):

    def enter_word(self, word):
        pass

    def click_on_the_search_button(self):
        pass

    def check_navigation_bar(self):
        pass