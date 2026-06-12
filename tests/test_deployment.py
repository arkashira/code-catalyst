import pytest
from deployment import Deployment, ScalingConfig, AnalyticsDashboard, UI

def test_deployment_scaling():
    deployment = Deployment("my_deployment", ScalingConfig(1, 10, 50))
    analytics_dashboard = AnalyticsDashboard()

    # Simulate scaling
    deployment.scale(60)
    analytics_dashboard.log_scaling_event(deployment, "CPU usage exceeded threshold")

    assert deployment.pod_count == 2
    assert len(analytics_dashboard.scaling_events) == 1

def test_adjust_scaling_thresholds():
    deployment = Deployment("my_deployment", ScalingConfig(1, 10, 50))
    ui = UI(deployment)

    # Adjust scaling thresholds via UI
    ui.adjust_scaling_thresholds(2, 15, 40)

    assert deployment.scaling_config.min_replicas == 2
    assert deployment.scaling_config.max_replicas == 15
    assert deployment.scaling_config.cpu_threshold == 40

def test_analytics_dashboard():
    analytics_dashboard = AnalyticsDashboard()
    deployment = Deployment("my_deployment", ScalingConfig(1, 10, 50))

    # Log scaling event
    analytics_dashboard.log_scaling_event(deployment, "CPU usage exceeded threshold")

    assert len(analytics_dashboard.scaling_events) == 1
    assert analytics_dashboard.scaling_events[0]["deployment"] == deployment.name
    assert analytics_dashboard.scaling_events[0]["reason"] == "CPU usage exceeded threshold"
    assert analytics_dashboard.scaling_events[0]["pod_count"] == deployment.pod_count
