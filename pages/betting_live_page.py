from pages.base_page import BasePage
from config.locators import BettingLiveLocators
from datetime import datetime as dt
import utils

class BettingLivePage(BasePage):

    page_locators = BettingLiveLocators

    def _fetch_live_events(self):
        events = utils.find_elements_by(self.driver, self.page_locators.live_event_info)
        live_events_names = [event.text.replace('\n', ' vs ') for event in events]
        return live_events_names

    def check_if_displayed(self):
        live_events_names = self._fetch_live_events()

        scheduled_events = utils.load_events_from_json()

        common_events = list(set(live_events_names) & set([event['name'] for event in scheduled_events]))

        for event in scheduled_events:
            event_name = event['name']
            if event_name in common_events:
                if event['status'] == "is_delayed":
                    event['status'] = "delayed"
                else:
                    event['status'] = "is_displayed"
            elif event['status'] in ['not_started', 'is_delayed']:
               self._update_not_shown_events(event)

        utils.save_events_to_json(scheduled_events)
        utils.remove_displayed_events_from_json()


    def _update_not_shown_events(self, event):
        event_startTime = dt.strptime(event['startTime'], '%Y-%m-%d %H:%M:%S')
        time_diff = (self.now - event_startTime).total_seconds()

        if time_diff < 0:
            event['status'] = 'not_started'
        elif time_diff < 60 * 20:
            event['status'] = 'is_delayed'
        else:
            event['status'] = 'dropped'

