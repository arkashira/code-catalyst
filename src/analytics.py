import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, date, timedelta
from typing import List, Dict, Iterable, Tuple


@dataclass(frozen=True)
class Event:
    """A single analytics event."""
    user_id: str
    timestamp: datetime
    session_length_seconds: int
    features_used: Tuple[str, ...]  # immutable collection of feature names


class AnalyticsDashboard:
    """In‑memory analytics dashboard with CSV export."""

    def __init__(self) -> None:
        # Store events sorted by timestamp for efficient queries.
        self._events: List[Event] = []

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #

    def add_event(self, event: Event) -> None:
        """Add a new analytics event."""
        # Insert while keeping list sorted (simple append + sort for small data).
        self._events.append(event)
        self._events.sort(key=lambda e: e.timestamp)

    def daily_active_users(self, target_date: date) -> int:
        """Return the number of distinct users that had any event on target_date."""
        users = {e.user_id for e in self._events_on_date(target_date)}
        return len(users)

    def average_session_length(self, target_date: date) -> float:
        """Return the average session length (seconds) for events on target_date.

        Returns 0.0 when there are no events for the date.
        """
        events = list(self._events_on_date(target_date))
        if not events:
            return 0.0
        total = sum(e.session_length_seconds for e in events)
        return total / len(events)

    def feature_usage(self, target_date: date) -> Dict[str, int]:
        """Return a mapping of feature name → count of usage on target_date."""
        counter: Counter = Counter()
        for e in self._events_on_date(target_date):
            counter.update(e.features_used)
        return dict(counter)

    def export_report(self, target_date: date, file_path: str) -> None:
        """Export a CSV report for the given date.

        The CSV contains rows:
            metric,value
        where metric can be:
            daily_active_users
            average_session_length_seconds
            feature:<feature_name>
        """
        dau = self.daily_active_users(target_date)
        avg_len = self.average_session_length(target_date)
        features = self.feature_usage(target_date)

        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["metric", "value"])
            writer.writerow(["daily_active_users", dau])
            writer.writerow(["average_session_length_seconds", f"{avg_len:.2f}"])
            for feat, cnt in sorted(features.items()):
                writer.writerow([f"feature:{feat}", cnt])

    # --------------------------------------------------------------------- #
    # Internal helpers
    # --------------------------------------------------------------------- #

    def _events_on_date(self, target_date: date) -> Iterable[Event]:
        """Yield events whose timestamp falls on target_date (UTC naive)."""
        start = datetime.combine(target_date, datetime.min.time())
        end = start + timedelta(days=1)
        for e in self._events:
            if start <= e.timestamp < end:
                yield e
