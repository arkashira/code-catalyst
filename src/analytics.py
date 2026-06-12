import datetime
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class DataPoint:
    timestamp: datetime.datetime
    value: float

class InMemoryTSDB:
    """ Very small in-memory time-series database. Stores data points per metric name. """
    def __init__(self) -> None:
        self._store: Dict[str, List[DataPoint]] = defaultdict(list)

    def add(self, metric: str, timestamp: datetime.datetime, value: float) -> None:
        """ Add a data point to the database. """
        self._store[metric].append(DataPoint(timestamp, value))

    def query(self, metric: str, start: datetime.datetime, end: datetime.datetime) -> List[DataPoint]:
        """ Return all data points for a metric between start and end (inclusive). """
        return [dp for dp in self._store.get(metric, []) if start <= dp.timestamp <= end]

class AnalyticsCollector:
    """ Collects events and writes them to the TSDB. """
    def __init__(self, tsdb: InMemoryTSDB) -> None:
        self.tsdb = tsdb

    def record_page_view(self, page: str, timestamp: datetime.datetime) -> None:
        """ Record a page view event. """
        self.tsdb.add("page_view", timestamp, 1)

    def record_session(self, duration_seconds: float, timestamp: datetime.datetime) -> None:
        """ Record a session duration event. """
        self.tsdb.add("session_duration", timestamp, duration_seconds)

    def record_feature_use(self, feature: str, timestamp: datetime.datetime) -> None:
        """ Record a feature usage event. """
        # Store feature name as part of metric key
        metric = f"feature_use:{feature}"
        self.tsdb.add(metric, timestamp, 1)

class Dashboard:
    """ Provides aggregated metrics for the last N minutes. """
    def __init__(self, tsdb: InMemoryTSDB, window_minutes: int = 5) -> None:
        self.tsdb = tsdb
        self.window = datetime.timedelta(minutes=window_minutes)

    def get_metrics(self, current_time: datetime.datetime) -> Dict[str, object]:
        """ Return aggregated metrics for the last `window_minutes` minutes. """
        start_time = current_time - self.window
        metrics: Dict[str, object] = {}
        # Page views count
        page_views = self.tsdb.query("page_view", start_time, current_time)
        metrics["page_views"] = len(page_views)
        # Average session duration
        sessions = self.tsdb.query("session_duration", start_time, current_time)
        if sessions:
            avg_duration = sum(dp.value for dp in sessions) / len(sessions)
        else:
            avg_duration = 0.0
        metrics["avg_session_duration"] = avg_duration
        # Feature usage counts
        feature_counts: Dict[str, int] = defaultdict(int)
        for metric_name in list(self.tsdb._store.keys()):
            if metric_name.startswith("feature_use:"):
                feature = metric_name.split(":", 1)[1]
                data_points = self.tsdb.query(metric_name, start_time, current_time)
                count = len(data_points)
                if count > 0:
                    feature_counts[feature] = count
        metrics["feature_usage"] = dict(feature_counts)
        return metrics
