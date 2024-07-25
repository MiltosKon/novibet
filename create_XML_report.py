import xml.etree.ElementTree as ET
import utils

class ReportGeneratorXML:
    def __init__(self):
        self.xml_file_path = './data/status_report.xml'

    def filter_delayed_or_dropped_matches(self, events):
        self.filtered_matches = \
            [target_event for target_event in events if target_event["status"] in ["delayed", "dropped"]]

    def generate_xml_report(self):
        root = ET.Element("matches")
        for match in self.filtered_matches:
            match_element = ET.SubElement(root, "event")
            ET.SubElement(match_element, "name").text = match["name"]
            ET.SubElement(match_element, "status").text = match["status"]
            ET.SubElement(match_element, "startTime").text = match["startTime"]

        xml_data = ET.tostring(root, encoding='utf-8', method='xml').decode()
        with open(self.xml_file_path, 'w') as xml_file:
            xml_file.write(xml_data)

        print("XML report created")

    def create_report(self):
        events = utils.load_events_from_json()
        self.filter_delayed_or_dropped_matches(events)
        self.generate_xml_report()
