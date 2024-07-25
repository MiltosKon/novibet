from datetime import timedelta as td
from pages.base_page import BasePage
from config.locators import LiveProgramLocators
import utils


class LiveProgramPage(BasePage):

    page_locators = LiveProgramLocators()

    def choose_soccer_matches(self):
        utils.find_element_by(self.driver, self.page_locators.event_type_dropdown).click()
        utils.find_element_by(self.driver, self.page_locators.event_type_soccer).click()

    def navigate_to_live_betting(self):
        utils.find_element_by(self.driver, self.page_locators.live_betting_button).click()

    def _parse_and_convert_time(self, time_str):

        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        if 'in' in time_str:
            time_parts = time_str.split()
            minutes_to_add = int(time_parts[1].strip("'"))
            timestamp = self.now + td(minutes=minutes_to_add)
            timestamp = timestamp.replace(second=0).strftime('%Y-%m-%d %H:%M:%S')
        elif ':' in time_str:
            time_parts = time_str.split()
            if len(time_parts) == 2: #  Day HH:MM
                target_day = days_of_week.index(time_parts[0])
                current_day = self.now.weekday()
                days_to_add = (target_day - current_day)
                target_date = self.now + td(days=days_to_add)
                time_str = time_parts[1]
                timestamp = f"{target_date.strftime('%Y-%m-%d')} {time_str}:00"

            else:  # HH:MM
                current_date = self.now.strftime('%Y-%m-%d')
                time = time_parts[0]
                timestamp = f"{current_date} {time}:00"
        else:
            raise ValueError(f"Unsupported time format: {time_str}")

        return timestamp

    def fetch_events(self):

        time_elements = utils.find_elements_by(self.driver, self.page_locators.start_time)
        name_elements = utils.find_elements_by(self.driver, self.page_locators.event_info)

        if len(time_elements) != len(name_elements):
            raise ValueError("Mismatch in number of time and name elements")

        schedule = []
        for time_element, name_element in zip(time_elements, name_elements):
            name = name_element.text.replace('\n', ' vs ')
            startTime = self._parse_and_convert_time(time_element.text)

            schedule.append({"name": name,"startTime": startTime,"status": "not_started"})

        utils.save_scheduled_events_to_json(schedule)
