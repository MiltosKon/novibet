
class BasePageLocators:
    setting_button = ('xpath', '//cm-icon[contains(@class,"Settings")]')
    change_language = staticmethod(lambda lang: ('xpath', f'//span[text()="{lang}"]'))
    login_popup_close_button = ('xpath', '//div[contains(@class,"registerOrLogin_closeButton")]')
    newsletter_popup_close_button =('xpath', '//button[contains(@class,"kumulos-action-button-cancel")]')
    interception_overlay = ('xpath', '//div[contains(@class,"cdk-overlay-backdrop")]')
    accept_cookies_button = ('xpath', '//button[contains(@class, "acceptCookies_button")]')

class LiveProgramLocators(BasePageLocators):
    event_type_dropdown = ('xpath', '//div[contains(@class,"scheduleFilters_sports")]')
    event_type_soccer = ('xpath', '//span[text()="Soccer"]')
    live_betting_button = ('xpath', '//span[text()="Live Betting"]')
    event_info = ('xpath', '//div[contains(@class,"event_info")]')
    start_time= ('xpath', '//span[contains(@class, "startTime")]')

class BettingLiveLocators(BasePageLocators):
    live_event_info = ('xpath', '//div[contains(@class,"eventLiveMatches_info")]')
