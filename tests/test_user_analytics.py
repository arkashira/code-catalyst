import pytest
from user_analytics import UserAnalytics, UserInteraction
import json

@pytest.fixture
def analytics():
    return UserAnalytics()

def test_log_interaction(analytics):
    analytics.log_interaction("user1", "home")
    assert len(analytics.interactions) == 1
    assert analytics.interactions[0].user_id == "user1"
    assert analytics.interactions[0].page_viewed == "home"

def test_get_metrics(analytics):
    analytics.log_interaction("user1", "home")
    analytics.log_interaction("user1", "home", clicked=True)
    analytics.log_interaction("user2", "about")
    metrics = analytics.get_metrics()
    assert metrics["page_views"]["home"] == 2
    assert metrics["clicks"]["home"] == 1
    assert metrics["click_through_rates"]["home"] == 0.5
    assert metrics["user_sessions"]["user1"] == 2
    assert metrics["user_sessions"]["user2"] == 1

def test_export_data(analytics, tmp_path):
    analytics.log_interaction("user1", "home")
    file_path = tmp_path / "analytics.json"
    analytics.export_data(str(file_path))
    with open(file_path, 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["user_id"] == "user1"
    assert data[0]["page_viewed"] == "home"

def test_get_dashboard_data(analytics):
    analytics.log_interaction("user1", "home")
    analytics.log_interaction("user1", "home", clicked=True)
    analytics.log_interaction("user2", "about")
    dashboard_data = analytics.get_dashboard_data()
    assert dashboard_data["total_page_views"] == 3
    assert dashboard_data["total_clicks"] == 1
    assert dashboard_data["total_users"] == 2
    assert dashboard_data["page_views_by_page"]["home"] == 2
    assert dashboard_data["click_through_rates_by_page"]["home"] == 0.5
    assert dashboard_data["user_sessions_by_user"]["user1"] == 2
