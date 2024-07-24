from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver_path = ChromeDriverManager().install()
    if driver_path:
        driver_name = driver_path.split('/')[-1]
        if driver_name != "chromedriver":
            driver_path = "\\".join(driver_path.split('/')[:-1] + ["chromedriver"])
    driver = webdriver.Chrome(service=Service(driver_path))
    return driver
