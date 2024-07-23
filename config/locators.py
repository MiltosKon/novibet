from selenium.webdriver.common.by import By

class BasePageLocators:
    setting_button = ('xpath', '//cm-icon[contains(@class,"Settings")]')
    change_language = lambda self, lang: ('xpath', f'//span[text()="{lang}"]')
    login_popup_close_button = ('xpath', '//div[contains(@class,"registerOrLogin_closeButton")]')
    newsletter_popup_close_button =('xpath', '//button[contains(@class,"kumulos-action-button-cancel")]')
    accept_cookies_button = ('xpath', '//button[contains(@class, "acceptCookies_button")]')


class LiveProgramLocators(BasePageLocators):
    event_type_dropdown = ('xpath', '//div[contains(@class,"scheduleFilters_sports")]')
    event_type_soccer = ('xpath', '//span[text()="Soccer"]')
    event_info = ('xpath', '//div[contains(@class,"event_info")]')
    start_time= ('xpath', '//span[contains(@class, "startTime")]')
