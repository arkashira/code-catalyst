from src.analytics import Analytics

class Dashboard:
    def __init__(self, analytics: Analytics):
        self.analytics = analytics

    def get_realtime_metrics(self):
        events = self.analytics.get_events()
        page_views = sum(1 for event in events if event.event_type == 'page_view')
        clicks = sum(1 for event in events if event.event_type == 'click')
        return {'page_views': page_views, 'clicks': clicks}
