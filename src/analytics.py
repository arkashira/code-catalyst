import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class PageView:
    user_id: int
    page_name: str

@dataclass
class UserEngagement:
    user_id: int
    engagement_score: float

class Analytics:
    def __init__(self):
        self.page_views = []
        self.user_engagement = {}

    def track_page_view(self, user_id: int, page_name: str):
        self.page_views.append(PageView(user_id, page_name))

    def calculate_user_engagement(self, user_id: int, engagement_score: float):
        self.user_engagement[user_id] = engagement_score

    def get_page_views(self) -> Dict[int, int]:
        page_views_per_user = {}
        for page_view in self.page_views:
            if page_view.user_id not in page_views_per_user:
                page_views_per_user[page_view.user_id] = 0
            page_views_per_user[page_view.user_id] += 1
        return page_views_per_user

    def get_user_engagement(self) -> Dict[int, float]:
        return self.user_engagement

class ABTesting:
    def __init__(self):
        self.experiments = {}

    def create_experiment(self, experiment_name: str):
        self.experiments[experiment_name] = {"variant_a": 0, "variant_b": 0}

    def update_experiment(self, experiment_name: str, variant: str):
        if experiment_name in self.experiments:
            if variant == "variant_a":
                self.experiments[experiment_name]["variant_a"] += 1
            elif variant == "variant_b":
                self.experiments[experiment_name]["variant_b"] += 1

    def get_experiment_results(self, experiment_name: str) -> Dict[str, int]:
        return self.experiments.get(experiment_name, {})

class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def send_notification(self, message: str):
        self.notifications.append(message)

    def get_notifications(self) -> list:
        return self.notifications
