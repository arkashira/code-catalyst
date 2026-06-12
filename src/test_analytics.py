import datetime
from unittest import TestCase
from analytics import AnalyticsCollector, Dashboard, InMemoryTSDB

class TestAnalyticsCollector(TestCase):
    def test_record_page_view(self):
        tsdb = InMemoryTSDB()
        collector = AnalyticsCollector(tsdb)
        timestamp = datetime.datetime(2022, 1, 1, 12, 0, 0)
        collector.record_page_view("home", timestamp)
        self.assertEqual(len(tsdb.query("page_view", timestamp, timestamp)), 1)

    def test_record_session(self):
        tsdb = InMemoryTSDB()
        collector = AnalyticsCollector(tsdb)
        timestamp = datetime.datetime(2022, 1, 1, 12, 0, 0)
        collector.record_session(10.0, timestamp)
        self.assertEqual(len(tsdb.query("session_duration", timestamp, timestamp)), 1)

    def test_record_feature_use(self):
        tsdb = InMemoryTSDB()
        collector = AnalyticsCollector(tsdb)
        timestamp = datetime.datetime(2022, 1, 1, 12, 0, 0)
        collector.record_feature_use("login", timestamp)
        self.assertEqual(len(tsdb.query("feature_use:login", timestamp, timestamp)), 1)

class TestDashboard(TestCase):
    def test_get_metrics(self):
        tsdb = InMemoryTSDB()
        collector = AnalyticsCollector(tsdb)
        dashboard = Dashboard(tsdb)
        timestamp = datetime.datetime(2022, 1, 1, 12, 0, 0)
        collector.record_page_view("home", timestamp)
        collector.record_session(10.0, timestamp)
        collector.record_feature_use("login", timestamp)
        metrics = dashboard.get_metrics(timestamp)
        self.assertEqual(metrics["page_views"], 1)
        self.assertEqual(metrics["avg_session_duration"], 10.0)
        self.assertEqual(metrics["feature_usage"], {"login": 1})

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
