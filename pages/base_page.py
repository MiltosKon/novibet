import utils
from config.locators import  BasePageLocators

class BasePage:

    page_locators = BasePageLocators()
    def __init__(self, driver):
        self.driver = driver

    def _handle_newsletter_popup(self):
        try:
            utils.find_element_by(self.driver, self.page_locators.newsletter_popup_close_button).click()
        except:
            pass

    def change_language(self, language):
        assert language in ["English",  "Ελληνικά"], "Not supported language"
        self._handle_newsletter_popup()
        utils.find_element_by(self.driver, self.page_locators.setting_button).click()
        utils.find_element_by(self.driver, self.page_locators.change_language(language)).click()
        utils.wait_url_to_contain(self.driver, '/en')

    def close_login_popup(self):
        self._handle_newsletter_popup()
        utils.find_element_by(self.driver, BasePageLocators.login_popup_close_button).click()
        return self

    def accept_cookies(self):
        utils.find_element_by(self.driver, BasePageLocators.accept_cookies_button).click()
        return self