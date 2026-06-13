import pytest
from src.prometheus_client import PrometheusClient, Metric

def test_register_metric():
    client = PrometheusClient()
    metric = Metric("cpu_usage", 0.5)
    client.register_metric(metric)
    assert client.metrics["cpu_usage"] == 0.5

def test_get_metrics():
    client = PrometheusClient()
    metric1 = Metric("cpu_usage", 0.5)
    metric2 = Metric("memory_usage", 0.2)
    client.register_metric(metric1)
    client.register_metric(metric2)
    metrics = client.get_metrics()
    assert len(metrics) == 2
    assert "cpu_usage 0.5" in metrics
    assert "memory_usage 0.2" in metrics
