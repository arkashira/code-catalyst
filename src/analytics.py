from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Event:
    timestamp: datetime
    event_type: str
    page_view: str

class Analytics:
    def __init__(self):
        self.events: List[Event] = []

    def track(self, event_type: str, page_view: str):
        event = Event(datetime.now(), event_type, page_view)
        self.events.append(event)
        return event

    def get_events(self):
        return self.events
