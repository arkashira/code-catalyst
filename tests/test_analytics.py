import pytest
from src.analytics import Analytics
from datetime import datetime

def test_track_event():
    analytics = Analytics()
    event = analytics.track('page_view', 'home')
    assert event.timestamp != datetime.min
    assert event.event_type == 'page_view'
    assert event.page_view == 'home'

def test_get_events():
    analytics = Analytics()
    analytics.track('page_view', 'home')
    analytics.track('click', 'button')
    assert len(analytics.get_events()) == 2
