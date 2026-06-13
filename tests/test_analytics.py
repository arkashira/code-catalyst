import pytest
from analytics import Analytics, Event

def test_add_event():
    analytics = Analytics()
    analytics.add_event('page_view', {'page': 'home'})
    assert len(analytics.events) == 1

def test_get_page_views():
    analytics = Analytics()
    analytics.add_event('page_view', {'page': 'home'})
    analytics.add_event('page_view', {'page': 'about'})
    assert analytics.get_page_views() == 2

def test_get_session_duration():
    analytics = Analytics()
    analytics.add_event('session_start', {'session_id': '123'})
    analytics.add_event('session_end', {'session_id': '123'})
    durations = list(analytics.get_session_duration())
    assert len(durations) == 1

def test_get_conversion_events():
    analytics = Analytics()
    analytics.add_event('conversion', {'product': 'A'})
    analytics.add_event('conversion', {'product': 'B'})
    assert analytics.get_conversion_events() == 2

def test_export_to_csv():
    analytics = Analytics()
    analytics.add_event('page_view', {'page': 'home'})
    analytics.export_to_csv()
    with open('analytics.csv', 'r') as f:
        assert f.read().startswith('timestamp,event_type,data\n')
