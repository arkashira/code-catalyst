import pytest
from src.analytics import Analytics
from src.dashboard import Dashboard

def test_main():
    analytics = Analytics()
    analytics.track('page_view', 'home')
    analytics.track('click', 'button')
    dashboard = Dashboard(analytics)
    metrics = dashboard.get_realtime_metrics()
    assert metrics['page_views'] == 1
    assert metrics['clicks'] == 1
