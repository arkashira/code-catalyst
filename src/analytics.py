import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class Event:
    type: str
    timestamp: datetime

class Analytics:
    def __init__(self, db_file):
        self.db_file = db_file
        self.events = []

    def collect(self, event_type):
        event = Event(event_type, datetime.now())
        self.events.append(event)

    def store(self):
        with open(self.db_file, 'w') as f:
            json.dump([{'type': e.type, 'timestamp': e.timestamp.isoformat()} for e in self.events], f)

    def display(self):
        page_views = sum(1 for e in self.events if e.type == 'page_view')
        button_clicks = sum(1 for e in self.events if e.type == 'button_click')
        form_submissions = sum(1 for e in self.events if e.type == 'form_submission')
        print(f'Page views: {page_views}')
        print(f'Button clicks: {button_clicks}')
        print(f'Form submissions: {form_submissions}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_file', default='analytics.json')
    args = parser.parse_args()
    analytics = Analytics(args.db_file)
    while True:
        print('1. Collect page view')
        print('2. Collect button click')
        print('3. Collect form submission')
        print('4. Display analytics')
        print('5. Store analytics')
        choice = input('Choose an option: ')
        if choice == '1':
            analytics.collect('page_view')
        elif choice == '2':
            analytics.collect('button_click')
        elif choice == '3':
            analytics.collect('form_submission')
        elif choice == '4':
            analytics.display()
        elif choice == '5':
            analytics.store()
        else:
            break

if __name__ == '__main__':
    main()
