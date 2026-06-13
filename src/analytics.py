import json
import time
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Event:
    timestamp: str
    event_type: str
    data: dict

class Analytics:
    def __init__(self):
        self.events = []

    def add_event(self, event_type: str, data: dict):
        event = Event(timestamp=datetime.now().isoformat(), event_type=event_type, data=data)
        self.events.append(event)

    def get_page_views(self):
        return len([event for event in self.events if event.event_type == 'page_view'])

    def get_session_duration(self):
        sessions = {}
        for event in self.events:
            if event.event_type == 'session_start':
                sessions[event.data['session_id']] = event.timestamp
            elif event.event_type == 'session_end':
                start_time = sessions.get(event.data['session_id'])
                if start_time:
                    duration = (datetime.fromisoformat(event.timestamp) - datetime.fromisoformat(start_time)).total_seconds()
                    yield duration

    def get_conversion_events(self):
        return len([event for event in self.events if event.event_type == 'conversion'])

    def export_to_csv(self):
        with open('analytics.csv', 'w') as f:
            f.write('timestamp,event_type,data\n')
            for event in self.events:
                f.write(f"{event.timestamp},{event.event_type},{json.dumps(event.data)}\n")

def main():
    analytics = Analytics()
    while True:
        # Simulate events
        analytics.add_event('page_view', {'page': 'home'})
        analytics.add_event('session_start', {'session_id': '123'})
        analytics.add_event('conversion', {'product': 'A'})
        analytics.add_event('session_end', {'session_id': '123'})

        # Display dashboard
        print(f"Page views: {analytics.get_page_views()}")
        print(f"Session duration: {list(analytics.get_session_duration())}")
        print(f"Conversion events: {analytics.get_conversion_events()}")

        # Export to CSV
        analytics.export_to_csv()

        time.sleep(30)

if __name__ == '__main__':
    main()
