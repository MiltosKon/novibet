import utils
from config.locators import  BasePageLocators

class BasePage:

    page_locators = BasePageLocators()
    def __init__(self, driver):
        self.driver = driver

    def change_language(self, language):
        assert language in ["English",  "Ελληνικά"], "Not supported language"
        utils.find_element_by(self.driver, self.page_locators.setting_button).click()
        utils.find_element_by(self.driver, self.page_locators.change_language(language)).click()
        utils.wait_url_to_contain(self.driver, '/en')

    def close_login_popup(self):
        utils.find_element_by(self.driver, BasePageLocators.login_popup_close_button).click()
        return self

    def accept_cookies(self):
        utils.find_element_by(self.driver, BasePageLocators.accept_cookies_button).click()
        return self