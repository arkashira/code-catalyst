import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class FeatureUsage:
    feature_name: str
    usage_count: int

@dataclass
class AnalyticsData:
    daily_active_users: int
    feature_usage: Dict[str, int]
    retention_curves: Dict[str, int]

class AnalyticsToolkit:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS analytics
            (date TEXT, feature_name TEXT, usage_count INTEGER)
        """)
        self.conn.commit()

    def store_analytics_data(self, data: AnalyticsData):
        self.cursor.execute("""
            INSERT INTO analytics (date, feature_name, usage_count)
            VALUES (?, ?, ?)
        """, (datetime.now().strftime("%Y-%m-%d"), "daily_active_users", data.daily_active_users))
        for feature, usage in data.feature_usage.items():
            self.cursor.execute("""
                INSERT INTO analytics (date, feature_name, usage_count)
                VALUES (?, ?, ?)
            """, (datetime.now().strftime("%Y-%m-%d"), feature, usage))
        self.conn.commit()

    def get_analytics_data(self) -> AnalyticsData:
        self.cursor.execute("""
            SELECT feature_name, usage_count
            FROM analytics
            WHERE date = ?
        """, (datetime.now().strftime("%Y-%m-%d"),))
        rows = self.cursor.fetchall()
        daily_active_users = 0
        feature_usage = {}
        for row in rows:
            if row[0] == "daily_active_users":
                daily_active_users = row[1]
            else:
                feature_usage[row[0]] = row[1]
        return AnalyticsData(daily_active_users, feature_usage, {})

    def close(self):
        self.conn.close()
