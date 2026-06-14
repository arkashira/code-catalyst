import os
import csv
from datetime import datetime, date, timedelta

import pytest

from analytics import AnalyticsDashboard, Event


@pytest.fixture
def dashboard() -> AnalyticsDashboard:
    return AnalyticsDashboard()


def make_event(user_id: str, days_offset: int, session_len: int, features) -> Event:
    ts = datetime.utcnow() + timedelta(days=days_offset)
    return Event(
        user_id=user_id,
        timestamp=ts,
        session_length_seconds=session_len,
        features_used=tuple(features),
    )


def test_daily_active_users_happy_path(dashboard: AnalyticsDashboard):
    today = date.today()
    dashboard.add_event(make_event("alice", 0, 120, ["search"]))
    dashboard.add_event(make_event("bob", 0, 300, ["upload", "download"]))
    dashboard.add_event(make_event("alice", 0, 60, ["download"]))  # same user again

    assert dashboard.daily_active_users(today) == 2  # alice & bob


def test_daily_active_users_no_events(dashboard: AnalyticsDashboard):
    assert dashboard.daily_active_users(date.today()) == 0


def test_average_session_length_happy_path(dashboard: AnalyticsDashboard):
    today = date.today()
    dashboard.add_event(make_event("u1", 0, 100, []))
    dashboard.add_event(make_event("u2", 0, 200, []))
    dashboard.add_event(make_event("u3", 0, 300, []))

    assert dashboard.average_session_length(today) == 200.0


def test_average_session_length_no_events(dashboard: AnalyticsDashboard):
    assert dashboard.average_session_length(date.today()) == 0.0


def test_feature_usage_happy_path(dashboard: AnalyticsDashboard):
    today = date.today()
    dashboard.add_event(make_event("u1", 0, 50, ["search", "upload"]))
    dashboard.add_event(make_event("u2", 0, 70, ["search"]))
    dashboard.add_event(make_event("u3", 0, 30, ["download", "upload"]))

    usage = dashboard.feature_usage(today)
    assert usage == {"search": 2, "upload": 2, "download": 1}


def test_feature_usage_no_events(dashboard: AnalyticsDashboard):
    assert dashboard.feature_usage(date.today()) == {}


def test_export_report_contents(tmp_path, dashboard: AnalyticsDashboard):
    today = date.today()
    dashboard.add_event(make_event("alice", 0, 120, ["search"]))
    dashboard.add_event(make_event("bob", 0, 300, ["upload", "download"]))
    dashboard.add_event(make_event("alice", 0, 60, ["download"]))

    csv_path = tmp_path / "report.csv"
    dashboard.export_report(today, str(csv_path))

    # Read back CSV and verify rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    # Header + 3 metric rows (DAU, avg, plus 3 features)
    assert rows[0] == ["metric", "value"]
    metric_dict = {row[0]: row[1] for row in rows[1:]}

    assert metric_dict["daily_active_users"] == "2"
    # average_session_length_seconds should be (120+300+60)/3 = 160.0
    assert metric_dict["average_session_length_seconds"] == "160.00"
    # Feature rows
    assert metric_dict["feature:download"] == "2"
    assert metric_dict["feature:search"] == "1"
    assert metric_dict["feature:upload"] == "1"
