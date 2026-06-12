import json
import dataclasses
import datetime
import time
from dataclasses import dataclass
from typing import List

@dataclass
class PageView:
    page: str
    timestamp: datetime.datetime

@dataclass
class UniqueVisitor:
    visitor_id: str
    timestamp: datetime.datetime

@dataclass
class SessionDuration:
    session_id: str
    duration: int

@dataclass
class ConversionEvent:
    event_type: str
    timestamp: datetime.datetime

class Analytics:
    def __init__(self):
        self.page_views = []
        self.unique_visitors = []
        self.session_durations = []
        self.conversion_events = []

    def add_page_view(self, page: str):
        self.page_views.append(PageView(page, datetime.datetime.now()))

    def add_unique_visitor(self, visitor_id: str):
        self.unique_visitors.append(UniqueVisitor(visitor_id, datetime.datetime.now()))

    def add_session_duration(self, session_id: str, duration: int):
        self.session_durations.append(SessionDuration(session_id, duration))

    def add_conversion_event(self, event_type: str):
        self.conversion_events.append(ConversionEvent(event_type, datetime.datetime.now()))

    def get_page_views(self):
        return len(self.page_views)

    def get_unique_visitors(self):
        return len(set([visitor.visitor_id for visitor in self.unique_visitors]))

    def get_session_durations(self):
        return [session.duration for session in self.session_durations]

    def get_conversion_events(self):
        return len(self.conversion_events)

    def export_to_csv(self):
        with open('analytics.csv', 'w') as f:
            f.write('Page Views,Unique Visitors,Session Durations,Conversion Events\n')
            f.write(f'{self.get_page_views()},{self.get_unique_visitors()},{sum(self.get_session_durations())},{self.get_conversion_events()}\n')

def refresh_data(analytics: Analytics):
    while True:
        time.sleep(300)  # refresh every 5 minutes
        analytics.export_to_csv()
