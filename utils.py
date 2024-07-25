import json
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException

def find_element_by(context, locator, timeout=20):
    strategy, locator_value = locator
    return WebDriverWait(context, timeout).until(EC.presence_of_element_located((strategy, locator_value)))

def find_elements_by(context, locator, timeout=10):
    strategy, locator_value = locator
    return WebDriverWait(context, timeout).until(EC.presence_of_all_elements_located((strategy, locator_value)))
def element_exists(context, locator):
    try:
        find_by, label = locator
        context.find_element(find_by, label)
        return True
    except NoSuchElementException:
        return False

def wait_url_to_contain(context, expected_url_part, timeout=10):
    WebDriverWait(context, timeout).until(EC.url_contains(expected_url_part))

def save_events_to_json(events):
    with open('.\data\events.json', 'w') as f:
        json.dump(events, f)
    print('Saved events to events.json')

def save_scheduled_events_to_json(events):

    file_path = './data/events.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_events = json.load(f)

        existing_event_names = {event['name'] for event in existing_events}
        new_events = [event for event in events if event['name'] not in existing_event_names]
        if new_events:
            print('New events logged')

        merged_events = existing_events + new_events

        with open(file_path, 'w') as f:
            json.dump(merged_events, f)

    else:
        save_events_to_json(events)


def load_events_from_json():
    file_path = './data/events.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    else:
        print("No events file found")

def remove_displayed_events_from_json( ):
    file_path = './data/events.json'

    with open(file_path, 'r') as file:
        events = json.load(file)

    filtered_events = [event for event in events if event['status'] != "is_displayed"]
    displayed_events = [event for event in events if event['status'] == "is_displayed"]
    if len(displayed_events) !=0:
        for displayed in displayed_events:
            print(f'Displayed event removed: {displayed["name"]}')
        print(f"Successfully removed displayed events")

    with open(file_path, 'w') as file:
        json.dump(filtered_events, file)
