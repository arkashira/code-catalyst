from deployment import Deployment, ScalingConfig
import pytest

def test_deployment_scaling():
    scaling_config = ScalingConfig(min_replicas=1, max_replicas=10, cpu_threshold=50)
    deployment = Deployment("test-deployment", scaling_config)

    # Test scaling up
    deployment.scale(60)
    assert deployment.pod_count == 2

    # Test scaling down
    deployment.scale(20)
    assert deployment.pod_count == 1

def test_deployment_logging():
    scaling_config = ScalingConfig(min_replicas=1, max_replicas=10, cpu_threshold=50)
    deployment = Deployment("test-deployment", scaling_config)

    deployment.log_scaling_event("Scaled up")
    # No assertion, just test that the log message is printed

def test_deployment_to_dict():
    scaling_config = ScalingConfig(min_replicas=1, max_replicas=10, cpu_threshold=50)
    deployment = Deployment("test-deployment", scaling_config)

    deployment_dict = deployment.to_dict()
    assert deployment_dict["name"] == "test-deployment"
    assert deployment_dict["scaling_config"]["min_replicas"] == 1
    assert deployment_dict["scaling_config"]["max_replicas"] == 10
    assert deployment_dict["scaling_config"]["cpu_threshold"] == 50
    assert deployment_dict["pod_count"] == 1
