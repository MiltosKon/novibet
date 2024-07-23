from utils import selection as sel
from config.locators import  BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def close_login_popup(self):
        sel.find_element_by(self.driver, BasePageLocators.login_popup_close_button).click()

    def accept_cookies(self):
        sel.find_element_by(self.driver, BasePageLocators.accept_cookies_button).click()