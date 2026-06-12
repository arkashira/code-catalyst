import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ScalingConfig:
    min_replicas: int
    max_replicas: int
    cpu_threshold: int

class Deployment:
    def __init__(self, name: str, scaling_config: ScalingConfig):
        self.name = name
        self.scaling_config = scaling_config
        self.pod_count = 1

    def scale(self, cpu_usage: int):
        if cpu_usage > self.scaling_config.cpu_threshold:
            self.pod_count = min(self.pod_count + 1, self.scaling_config.max_replicas)
        elif cpu_usage < self.scaling_config.cpu_threshold / 2:
            self.pod_count = max(self.pod_count - 1, self.scaling_config.min_replicas)

    def to_dict(self):
        return {
            "name": self.name,
            "scaling_config": {
                "min_replicas": self.scaling_config.min_replicas,
                "max_replicas": self.scaling_config.max_replicas,
                "cpu_threshold": self.scaling_config.cpu_threshold
            },
            "pod_count": self.pod_count
        }

class AnalyticsDashboard:
    def __init__(self):
        self.scaling_events = []

    def log_scaling_event(self, deployment: Deployment, reason: str):
        self.scaling_events.append({
            "deployment": deployment.name,
            "reason": reason,
            "pod_count": deployment.pod_count
        })

    def to_dict(self):
        return {
            "scaling_events": self.scaling_events
        }

class UI:
    def __init__(self, deployment: Deployment):
        self.deployment = deployment

    def adjust_scaling_thresholds(self, min_replicas: int, max_replicas: int, cpu_threshold: int):
        self.deployment.scaling_config = ScalingConfig(min_replicas, max_replicas, cpu_threshold)

def main():
    deployment = Deployment("my_deployment", ScalingConfig(1, 10, 50))
    analytics_dashboard = AnalyticsDashboard()
    ui = UI(deployment)

    # Simulate scaling
    deployment.scale(60)
    analytics_dashboard.log_scaling_event(deployment, "CPU usage exceeded threshold")

    # Adjust scaling thresholds via UI
    ui.adjust_scaling_thresholds(2, 15, 40)

    # Print deployment and analytics dashboard data
    print(json.dumps(deployment.to_dict(), indent=4))
    print(json.dumps(analytics_dashboard.to_dict(), indent=4))

if __name__ == "__main__":
    main()
