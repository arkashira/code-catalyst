import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Event:
    timestamp: datetime
    event_type: str
    data: dict

class Analytics:
    def __init__(self):
        self.events = []

    def track(self, event_type: str, data: dict):
        event = Event(timestamp=datetime.now(), event_type=event_type, data=data)
        self.events.append(event)

    def get_daily_views(self):
        daily_views = {}
        for event in self.events:
            if event.event_type == 'page_view':
                date = event.timestamp.date()
                if date in daily_views:
                    daily_views[date] += 1
                else:
                    daily_views[date] = 1
        return daily_views

    def get_weekly_views(self):
        weekly_views = {}
        for event in self.events:
            if event.event_type == 'page_view':
                week = event.timestamp.isocalendar()[1]
                if week in weekly_views:
                    weekly_views[week] += 1
                else:
                    weekly_views[week] = 1
        return weekly_views

    def get_button_clicks(self):
        button_clicks = {}
        for event in self.events:
            if event.event_type == 'button_click':
                button_id = event.data.get('button_id')
                if button_id in button_clicks:
                    button_clicks[button_id] += 1
                else:
                    button_clicks[button_id] = 1
        return button_clicks

    def get_form_submissions(self):
        form_submissions = {}
        for event in self.events:
            if event.event_type == 'form_submission':
                form_id = event.data.get('form_id')
                if form_id in form_submissions:
                    form_submissions[form_id] += 1
                else:
                    form_submissions[form_id] = 1
        return form_submissions

    def get_dashboard_data(self):
        daily_views = self.get_daily_views()
        weekly_views = self.get_weekly_views()
        button_clicks = self.get_button_clicks()
        form_submissions = self.get_form_submissions()
        return {
            'daily_views': daily_views,
            'weekly_views': weekly_views,
            'button_clicks': button_clicks,
            'form_submissions': form_submissions
        }
