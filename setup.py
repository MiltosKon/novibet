from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = Options()
    # options.add_argument("--start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    driver_path = ChromeDriverManager().install().replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver.exe")
    driver = webdriver.Chrome(service=Service(driver_path ), options=options)
    return driver
