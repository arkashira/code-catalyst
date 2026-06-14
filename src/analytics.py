import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class UserEngagement:
    daily_active_users: int
    session_length: float
    feature_usage: dict

class AnalyticsDashboard:
    def __init__(self):
        self.data = []

    def add_data(self, engagement: UserEngagement):
        self.data.append(engagement)

    def get_daily_active_users(self) -> List[int]:
        return [e.daily_active_users for e in self.data]

    def get_session_length(self) -> List[float]:
        return [e.session_length for e in self.data]

    def get_feature_usage(self) -> List[dict]:
        return [e.feature_usage for e in self.data]

    def export_csv(self, filename: str):
        with open(filename, 'w') as f:
            f.write('Date,Daily Active Users,Session Length,Feature Usage\n')
            for i, e in enumerate(self.data):
                f.write(f'{datetime.now() - timedelta(days=i)},'
                        f'{e.daily_active_users},{e.session_length},'
                        f'{json.dumps(e.feature_usage)}\n')

class InMemoryDatabase:
    def __init__(self):
        self.data = []

    def insert(self, engagement: UserEngagement):
        self.data.append(engagement)

    def get_data(self) -> List[UserEngagement]:
        return self.data

def refresh_data(db: InMemoryDatabase, dashboard: AnalyticsDashboard):
    data = db.get_data()
    if data:
        dashboard.add_data(data[-1])  # Add the latest data to the dashboard
