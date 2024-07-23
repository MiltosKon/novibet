import json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element_by(context, locator, timeout=10):
    strategy, locator_value = locator
    return WebDriverWait(context, timeout).until(EC.presence_of_element_located((strategy, locator_value)))

def find_elements_by(context, locator, timeout=10):
    strategy, locator_value = locator
    return WebDriverWait(context, timeout).until(EC.presence_of_all_elements_located((strategy, locator_value)))

def wait_url_to_contain(context, expected_url_part, timeout=10):
    WebDriverWait(context, timeout).until(EC.url_contains(expected_url_part))

def save_events_to_json(events):
    with open('.\data\events.json', 'w') as f:
        json.dump(events, f)
    print('Saved events to events.json')