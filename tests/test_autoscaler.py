import pytest
from src.autoscaler import Autoscaler, ScalingConfig

def test_scale():
    config = ScalingConfig(min_replicas=1, max_replicas=5, cpu_threshold=0.8)
    autoscaler = Autoscaler(config)
    cpu_usage = 0.9
    replicas = autoscaler.scale(cpu_usage)
    assert replicas == 5

def test_scale_below_threshold():
    config = ScalingConfig(min_replicas=1, max_replicas=5, cpu_threshold=0.8)
    autoscaler = Autoscaler(config)
    cpu_usage = 0.7
    replicas = autoscaler.scale(cpu_usage)
    assert replicas == 1
