import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict
from analytics import AnalyticsToolkit, AnalyticsData

@dataclass
class DashboardData:
    daily_active_users: int
    feature_usage: Dict[str, int]
    retention_curves: Dict[str, int]

class Dashboard:
    def __init__(self, analytics_toolkit: AnalyticsToolkit):
        self.analytics_toolkit = analytics_toolkit

    def get_dashboard_data(self) -> DashboardData:
        analytics_data = self.analytics_toolkit.get_analytics_data()
        return DashboardData(analytics_data.daily_active_users, analytics_data.feature_usage, analytics_data.retention_curves)

    def refresh_data(self):
        # Simulate data refresh every 5 minutes
        import time
        while True:
            analytics_data = self.analytics_toolkit.get_analytics_data()
            print(f"Daily Active Users: {analytics_data.daily_active_users}")
            print("Feature Usage:")
            for feature, usage in analytics_data.feature_usage.items():
                print(f"{feature}: {usage}")
            time.sleep(300)
