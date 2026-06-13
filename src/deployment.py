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

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "scaling_config": {
                "min_replicas": self.scaling_config.min_replicas,
                "max_replicas": self.scaling_config.max_replicas,
                "cpu_threshold": self.scaling_config.cpu_threshold
            },
            "pod_count": self.pod_count
        }

    def log_scaling_event(self, event: str):
        print(f"Scaling event: {event} for deployment {self.name}")
