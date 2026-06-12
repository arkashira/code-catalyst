import pytest
from analytics import Analytics, PageView, UniqueVisitor, SessionDuration, ConversionEvent

def test_page_views():
    analytics = Analytics()
    analytics.add_page_view('home')
    analytics.add_page_view('about')
    assert analytics.get_page_views() == 2

def test_unique_visitors():
    analytics = Analytics()
    analytics.add_unique_visitor('visitor1')
    analytics.add_unique_visitor('visitor2')
    analytics.add_unique_visitor('visitor1')
    assert analytics.get_unique_visitors() == 2

def test_session_durations():
    analytics = Analytics()
    analytics.add_session_duration('session1', 10)
    analytics.add_session_duration('session2', 20)
    assert analytics.get_session_durations() == [10, 20]

def test_conversion_events():
    analytics = Analytics()
    analytics.add_conversion_event('click')
    analytics.add_conversion_event('click')
    assert analytics.get_conversion_events() == 2

def test_export_to_csv(tmp_path):
    analytics = Analytics()
    analytics.add_page_view('home')
    analytics.add_unique_visitor('visitor1')
    analytics.add_session_duration('session1', 10)
    analytics.add_conversion_event('click')
    analytics.export_to_csv()
    with open('analytics.csv', 'r') as f:
        assert f.read() == 'Page Views,Unique Visitors,Session Durations,Conversion Events\n1,1,10,1\n'
