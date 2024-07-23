from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from config.urls import Urls as urls
from pages.live_program_page import LiveProgramPage
import utils

#start time
st = time.time()


options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(urls.live_schedule_url)

live_program_page_instance = LiveProgramPage(driver)

live_program_page_instance.close_login_popup().accept_cookies().change_language("English")

live_program_page_instance.choose_soccer_matches()
live_program_events = live_program_page_instance.fetch_events()
utils.save_events_to_json(live_program_events)

driver.quit()

# end time
et = time.time()
res = (et - st)*1000
print('Execution time:', res, 'ms')