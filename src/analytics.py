import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserInteraction:
    page_view: int
    click_through_rate: float
    user_session: int

class Analytics:
    def __init__(self):
        self.interactions = []

    def add_interaction(self, interaction):
        self.interactions.append(interaction)

    def get_metrics(self):
        total_page_views = sum(i.page_view for i in self.interactions)
        total_click_through_rate = sum(i.click_through_rate for i in self.interactions) / len(self.interactions) if self.interactions else 0
        total_user_sessions = sum(i.user_session for i in self.interactions)
        return {
            "page_views": total_page_views,
            "click_through_rate": total_click_through_rate,
            "user_sessions": total_user_sessions
        }

    def export_data(self):
        data = [{"page_view": i.page_view, "click_through_rate": i.click_through_rate, "user_session": i.user_session} for i in self.interactions]
        return json.dumps(data, indent=4)

    def display_dashboard(self):
        metrics = self.get_metrics()
        print("Dashboard:")
        print(f"Page Views: {metrics['page_views']}")
        print(f"Click Through Rate: {metrics['click_through_rate']:.2f}")
        print(f"User Sessions: {metrics['user_sessions']}")
