from analytics import AnalyticsDashboard, UserEngagement, InMemoryDatabase, refresh_data
import pytest

def test_get_daily_active_users():
    dashboard = AnalyticsDashboard()
    engagement1 = UserEngagement(10, 30.0, {'feature1': 5, 'feature2': 3})
    engagement2 = UserEngagement(15, 45.0, {'feature1': 7, 'feature2': 5})
    dashboard.add_data(engagement1)
    dashboard.add_data(engagement2)
    assert dashboard.get_daily_active_users() == [10, 15]

def test_get_session_length():
    dashboard = AnalyticsDashboard()
    engagement1 = UserEngagement(10, 30.0, {'feature1': 5, 'feature2': 3})
    engagement2 = UserEngagement(15, 45.0, {'feature1': 7, 'feature2': 5})
    dashboard.add_data(engagement1)
    dashboard.add_data(engagement2)
    assert dashboard.get_session_length() == [30.0, 45.0]

def test_get_feature_usage():
    dashboard = AnalyticsDashboard()
    engagement1 = UserEngagement(10, 30.0, {'feature1': 5, 'feature2': 3})
    engagement2 = UserEngagement(15, 45.0, {'feature1': 7, 'feature2': 5})
    dashboard.add_data(engagement1)
    dashboard.add_data(engagement2)
    assert dashboard.get_feature_usage() == [{'feature1': 5, 'feature2': 3}, {'feature1': 7, 'feature2': 5}]

def test_export_csv(tmp_path):
    dashboard = AnalyticsDashboard()
    engagement1 = UserEngagement(10, 30.0, {'feature1': 5, 'feature2': 3})
    engagement2 = UserEngagement(15, 45.0, {'feature1': 7, 'feature2': 5})
    dashboard.add_data(engagement1)
    dashboard.add_data(engagement2)
    filename = tmp_path / 'analytics.csv'
    dashboard.export_csv(str(filename))
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 3
        assert lines[0].strip() == 'Date,Daily Active Users,Session Length,Feature Usage'
        assert lines[1].strip().startswith('202')
        assert lines[2].strip().startswith('202')

def test_refresh_data():
    db = InMemoryDatabase()
    dashboard = AnalyticsDashboard()
    engagement1 = UserEngagement(10, 30.0, {'feature1': 5, 'feature2': 3})
    db.insert(engagement1)
    refresh_data(db, dashboard)
    assert len(dashboard.data) == 1
    assert dashboard.data[0].daily_active_users == 10
