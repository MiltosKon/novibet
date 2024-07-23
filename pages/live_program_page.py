from datetime import datetime, timedelta
from pages.base_page import BasePage
from config.locators import LiveProgramLocators
import utils


class LiveProgramPage(BasePage):

    page_locators = LiveProgramLocators()
    current_gmt2_time = datetime.utcnow() + timedelta(hours=3)

    def choose_soccer_matches(self):
        utils.find_element_by(self.driver, self.page_locators.event_type_dropdown).click()
        utils.find_element_by(self.driver, self.page_locators.event_type_soccer).click()

    def _convert_to_gmt2(self, time_str):

        if 'in' in time_str:
            time_parts = time_str.split()
            minutes_to_add = int(time_parts[1].strip("'"))
            converted_time = self.current_gmt2_time + timedelta(minutes=minutes_to_add)
        elif ':' in time_str:

            if len(time_str.split()) == 2:  #  Day HH:MM
                parsed_time = datetime.strptime(time_str, "%a %H:%M")
            else:  # HH:MM
                parsed_time = datetime.strptime(time_str, "%H:%M")

            parsed_time = parsed_time.replace(year=self.current_gmt2_time.year, month=self.current_gmt2_time.month, day=self.current_gmt2_time.day)
            converted_time = parsed_time + timedelta(hours=3)  # convert to GMT+2
        else:
            raise ValueError(f"Unsupported time format: {time_str}")

        return converted_time.strftime("%Y-%m-%d %H:%M:%S")

    def fetch_events(self):

        time_elements = utils.find_elements_by(self.driver, self.page_locators.start_time)
        name_elements = utils.find_elements_by(self.driver, self.page_locators.event_info)

        if len(time_elements) != len(name_elements):
            raise ValueError("Mismatch in number of time and name elements")

        schedule = []
        for time_element, name_element in zip(time_elements, name_elements):
            name = name_element.text.replace('\n', ' vs ')
            startTime = self._convert_to_gmt2(time_element.text)

            schedule.append({"name": name,"startTime": startTime,"status": "not_started"})

        return schedule
