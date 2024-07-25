from config.urls import Urls as urls
from pages.betting_live_page import BettingLivePage
from setup import setup_driver

def main():
    driver = setup_driver()
    try:
        driver.get(urls.betting_live_url)
        betting_live_page_instance = BettingLivePage(driver)
        betting_live_page_instance.close_login_popup().accept_cookies().change_language("English")
        betting_live_page_instance.check_if_displayed()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()