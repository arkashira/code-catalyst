import json
import time
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Metrics:
    visits: int = 0
    conversions: int = 0
    retention: int = 0

class Tracker:
    def __init__(self):
        self.metrics = Metrics()
        self.last_update = datetime.now()

    def update_metrics(self, visits=0, conversions=0, retention=0):
        self.metrics.visits += visits
        self.metrics.conversions += conversions
        self.metrics.retention += retention
        self.last_update = datetime.now()

    def get_metrics(self):
        return self.metrics

    def export_metrics(self):
        return {
            "visits": self.metrics.visits,
            "conversions": self.metrics.conversions,
            "retention": self.metrics.retention,
        }

    def track_user_action(self, action):
        if action == "visit":
            self.update_metrics(visits=1)
        elif action == "conversion":
            self.update_metrics(conversions=1)
        elif action == "retention":
            self.update_metrics(retention=1)

    def update_metrics_periodically(self):
        while True:
            time.sleep(300)  # 5 minutes
            self.update_metrics()

def main():
    tracker = Tracker()
    tracker.track_user_action("visit")
    tracker.track_user_action("conversion")
    tracker.track_user_action("retention")
    print(tracker.get_metrics())
    print(json.dumps(tracker.export_metrics()))

if __name__ == "__main__":
    main()
