import pytest
from analytics import Analytics, Event

def test_track_page_view():
    analytics = Analytics()
    analytics.track('page_view', {})
    assert len(analytics.events) == 1
    assert analytics.events[0].event_type == 'page_view'

def test_get_daily_views():
    analytics = Analytics()
    analytics.track('page_view', {})
    analytics.track('page_view', {})
    daily_views = analytics.get_daily_views()
    assert len(daily_views) == 1
    assert list(daily_views.values())[0] == 2

def test_get_weekly_views():
    analytics = Analytics()
    analytics.track('page_view', {})
    analytics.track('page_view', {})
    weekly_views = analytics.get_weekly_views()
    assert len(weekly_views) == 1
    assert list(weekly_views.values())[0] == 2

def test_get_button_clicks():
    analytics = Analytics()
    analytics.track('button_click', {'button_id': 'button1'})
    analytics.track('button_click', {'button_id': 'button1'})
    analytics.track('button_click', {'button_id': 'button2'})
    button_clicks = analytics.get_button_clicks()
    assert len(button_clicks) == 2
    assert button_clicks['button1'] == 2
    assert button_clicks['button2'] == 1

def test_get_form_submissions():
    analytics = Analytics()
    analytics.track('form_submission', {'form_id': 'form1'})
    analytics.track('form_submission', {'form_id': 'form1'})
    analytics.track('form_submission', {'form_id': 'form2'})
    form_submissions = analytics.get_form_submissions()
    assert len(form_submissions) == 2
    assert form_submissions['form1'] == 2
    assert form_submissions['form2'] == 1

def test_get_dashboard_data():
    analytics = Analytics()
    analytics.track('page_view', {})
    analytics.track('button_click', {'button_id': 'button1'})
    analytics.track('form_submission', {'form_id': 'form1'})
    dashboard_data = analytics.get_dashboard_data()
    assert 'daily_views' in dashboard_data
    assert 'weekly_views' in dashboard_data
    assert 'button_clicks' in dashboard_data
    assert 'form_submissions' in dashboard_data
