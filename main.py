import time
import logging
import traceback
import polling
from config.urls import Urls as urls
from create_XML_report import ReportGeneratorXML
from pages.live_program_page import LiveProgramPage
from pages.betting_live_page import BettingLivePage
from setup import setup_driver

def main():
    driver = setup_driver()
    try:
        st = time.time()
        driver.get(urls.live_schedule_url)
        live_program_page_instance = LiveProgramPage(driver)
        live_program_page_instance.close_login_popup().accept_cookies().change_language("English")
        live_program_page_instance.choose_soccer_matches()
        live_program_page_instance.fetch_events()

        driver.get(urls.betting_live_url)
        betting_live_page_instance = BettingLivePage(driver)
        betting_live_page_instance.change_language("English")
        betting_live_page_instance.check_if_displayed()

        report_generator = ReportGeneratorXML()
        report_generator.create_report()
    except:
        driver.get_screenshot_as_file("./data/screenshot.png")
        logging.error(f'Run failed because of:\n {traceback.print_exc()} \n  screenshot has been saved for review')
    finally:
        logging.info(f"Execution time: {time.time() - st:.2f} seconds")
        driver.quit()


if __name__ == "__main__":
    # change step for your desired interval (in seconds)
    polling.poll(main, step=60, poll_forever=True)
    