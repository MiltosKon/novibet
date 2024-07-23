from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element_by(context, locator, timeout=5):
    strategy, locator_value = locator
    return WebDriverWait(context, timeout).until(EC.presence_of_element_located((strategy, locator_value)))
def find_elements_by(context, locator):
    strategy, locator_value = locator
    return WebDriverWait(context, 20).until(EC.presence_of_all_elements_located((strategy, locator_value))    )