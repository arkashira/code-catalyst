import pytest
from src.analytics import AnalyticsToolkit, AnalyticsData
from src.dashboard import Dashboard

def test_analytics_toolkit():
    analytics_toolkit = AnalyticsToolkit(":memory:")
    analytics_data = AnalyticsData(100, {"feature1": 50, "feature2": 30}, {})
    analytics_toolkit.store_analytics_data(analytics_data)
    retrieved_data = analytics_toolkit.get_analytics_data()
    assert retrieved_data.daily_active_users == 100
    assert retrieved_data.feature_usage == {"feature1": 50, "feature2": 30}

def test_dashboard():
    analytics_toolkit = AnalyticsToolkit(":memory:")
    dashboard = Dashboard(analytics_toolkit)
    analytics_data = AnalyticsData(100, {"feature1": 50, "feature2": 30}, {})
    analytics_toolkit.store_analytics_data(analytics_data)
    dashboard_data = dashboard.get_dashboard_data()
    assert dashboard_data.daily_active_users == 100
    assert dashboard_data.feature_usage == {"feature1": 50, "feature2": 30}
