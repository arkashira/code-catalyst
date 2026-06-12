import json
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
from collections import defaultdict

@dataclass
class UserInteraction:
    user_id: str
    page_viewed: str
    timestamp: float
    clicked: bool = False

class UserAnalytics:
    def __init__(self):
        self.interactions: List[UserInteraction] = []
        self.metrics = {
            "page_views": defaultdict(int),
            "clicks": defaultdict(int),
            "user_sessions": defaultdict(list)
        }

    def log_interaction(self, user_id: str, page_viewed: str, clicked: bool = False) -> None:
        interaction = UserInteraction(user_id, page_viewed, time.time(), clicked)
        self.interactions.append(interaction)
        self._update_metrics(interaction)

    def _update_metrics(self, interaction: UserInteraction) -> None:
        self.metrics["page_views"][interaction.page_viewed] += 1
        if interaction.clicked:
            self.metrics["clicks"][interaction.page_viewed] += 1
        self.metrics["user_sessions"][interaction.user_id].append(interaction.timestamp)

    def get_metrics(self) -> Dict:
        return {
            "page_views": dict(self.metrics["page_views"]),
            "clicks": dict(self.metrics["clicks"]),
            "click_through_rates": { page: self.metrics["clicks"][page] / self.metrics["page_views"][page] for page in self.metrics["page_views"] },
            "user_sessions": { user: len(sessions) for user, sessions in self.metrics["user_sessions"].items() }
        }

    def export_data(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            json.dump([asdict(interaction) for interaction in self.interactions], f, indent=2)

    def get_dashboard_data(self) -> Dict:
        metrics = self.get_metrics()
        return {
            "total_page_views": sum(metrics["page_views"].values()),
            "total_clicks": sum(metrics["clicks"].values()),
            "total_users": len(metrics["user_sessions"]),
            "page_views_by_page": metrics["page_views"],
            "click_through_rates_by_page": metrics["click_through_rates"],
            "user_sessions_by_user": metrics["user_sessions"]
        }
