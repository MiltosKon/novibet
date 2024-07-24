from config.urls import Urls as urls
from pages.live_program_page import LiveProgramPage
import utils
from setup import setup_driver

def main():
    driver = setup_driver()
    try:
        driver.get(urls.live_schedule_url)
        live_program_page_instance = LiveProgramPage(driver)
        live_program_page_instance.close_login_popup().accept_cookies().change_language("English")
        live_program_page_instance.choose_soccer_matches()
        live_program_events = live_program_page_instance.fetch_events()
        utils.save_events_to_json(live_program_events)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()