import argparse
import json
from dataclasses import dataclass

@dataclass
class ScalingConfig:
    min_replicas: int
    max_replicas: int
    cpu_threshold: float

class Autoscaler:
    def __init__(self, config):
        self.config = config

    def scale(self, cpu_usage):
        if cpu_usage > self.config.cpu_threshold:
            return self.config.max_replicas
        else:
            return self.config.min_replicas

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to scaling config file")
    args = parser.parse_args()
    with open(args.config, "r") as f:
        config = json.load(f)
    scaling_config = ScalingConfig(
        min_replicas=config["min_replicas"],
        max_replicas=config["max_replicas"],
        cpu_threshold=config["cpu_threshold"],
    )
    autoscaler = Autoscaler(scaling_config)
    cpu_usage = 0.5  # Replace with actual CPU usage
    replicas = autoscaler.scale(cpu_usage)
    print(f"Scaling to {replicas} replicas")

if __name__ == "__main__":
    main()
