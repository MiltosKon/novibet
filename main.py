import time
import traceback
from config.urls import Urls as urls
from create_XML_report import ReportGeneratorXML
from pages.live_program_page import LiveProgramPage
from pages.betting_live_page import BettingLivePage
from setup import setup_driver

st = time.time()

def main():

    driver = setup_driver()
    try:
        driver.get(urls.live_schedule_url)
        live_program_page_instance = LiveProgramPage(driver)
        live_program_page_instance.close_login_popup().accept_cookies().change_language("English")
        live_program_page_instance.choose_soccer_matches()
        live_program_page_instance.fetch_events()

        driver.get(urls.betting_live_url)
        betting_live_page_instance = BettingLivePage(driver)
        betting_live_page_instance.check_if_displayed()

        report_generator = ReportGeneratorXML()
        report_generator.create_report()
    except Exception as e:
        print(f'Message: {e}')
        print(traceback.print_exc() )
        print('[FAIL] see screenshot for details')
        driver.get_screenshot_as_file(f"./data/screenshot_{time.strftime('%H.%M', time.localtime())}.png")
    finally:
        driver.quit()
        exec_time = time.time() - st
        print(f"Execution time: {exec_time:.2f} seconds")


if __name__ == "__main__":
    main()