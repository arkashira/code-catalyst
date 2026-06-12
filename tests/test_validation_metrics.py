from validation_metrics import ValidationMetricsDashboard, Metric
from datetime import datetime, timedelta

def test_add_metric():
    dashboard = ValidationMetricsDashboard()
    metric = Metric("pageviews", 10, datetime.now())
    dashboard.add_metric(metric)
    assert len(dashboard.metrics["pageviews"]) == 1

def test_get_metrics():
    dashboard = ValidationMetricsDashboard()
    metric1 = Metric("pageviews", 10, datetime.now())
    metric2 = Metric("pageviews", 20, datetime.now() + timedelta(days=1))
    dashboard.add_metric(metric1)
    dashboard.add_metric(metric2)
    metrics = dashboard.get_metrics()
    assert metrics["pageviews"] == 30

def test_get_metrics_with_time_filter():
    dashboard = ValidationMetricsDashboard()
    metric1 = Metric("pageviews", 10, datetime.now())
    metric2 = Metric("pageviews", 20, datetime.now() + timedelta(days=1))
    dashboard.add_metric(metric1)
    dashboard.add_metric(metric2)
    start_time = datetime.now()
    end_time = datetime.now() + timedelta(days=1)
    metrics = dashboard.get_metrics(start_time, end_time)
    assert metrics["pageviews"] == 30

def test_get_metrics_with_segment_filter():
    dashboard = ValidationMetricsDashboard()
    metric1 = Metric("pageviews:segment1", 10, datetime.now())
    metric2 = Metric("pageviews:segment2", 20, datetime.now() + timedelta(days=1))
    dashboard.add_metric(metric1)
    dashboard.add_metric(metric2)
    metrics = dashboard.get_metrics(segment="segment1")
    assert metrics["pageviews:segment1"] == 10

def test_to_json():
    dashboard = ValidationMetricsDashboard()
    metric1 = Metric("pageviews", 10, datetime.now())
    metric2 = Metric("pageviews", 20, datetime.now() + timedelta(days=1))
    dashboard.add_metric(metric1)
    dashboard.add_metric(metric2)
    json_string = dashboard.to_json()
    assert json_string == '{"pageviews": 30}'
