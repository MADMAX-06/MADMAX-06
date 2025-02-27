from BaseApp import BasePage
from selenium.webdriver.common.by import By


class CitilinkSeacrhLocators:
    LOCATOR_CITILINK_SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='search']")
    LOCATOR_CITILINK_SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOCATOR_CITILINK_NAVIGATION_BAR = (By.CLASS_NAME, "div[data-meta-name='HeaderTopLinks']")
    LOCATOR_CITILINK_AUTH = (By.CSS_SELECTOR, "div[data-meta-name='UserButtonContainer']")
    LOCATOR_CITILINK_AUTH_EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")


class SearchHelper(BasePage):

    def enter_word(self, word):
        auth_email_field = self.find_element(CitilinkSeacrhLocators.LOCATOR_CITILINK_AUTH_EMAIL_FIELD)
        auth_email_field.click()
        auth_email_field.send_keys(word)
        return auth_email_field

    def click_on_the_search_button(self):
        pass

    def check_navigation_bar(self):
        pass