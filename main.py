from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from config.urls import Urls as urls
from pages.base_page import BasePage


options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(urls.live_schedule_url)

base_page_instance = BasePage(driver)
base_page_instance.close_login_popup()
base_page_instance.accept_cookies()


time.sleep(10)
driver.quit()
