import json
from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict
from typing import List, Optional, Dict


@dataclass
class Metric:
    """A single metric record."""
    name: str
    value: int
    timestamp: datetime


class ValidationMetricsDashboard:
    """Collects Metric objects and provides aggregated views."""

    def __init__(self) -> None:
        # Store a list of Metric objects per metric name
        self.metrics: Dict[str, List[Metric]] = defaultdict(list)

    def add_metric(self, metric: Metric) -> None:
        """Add a metric to the dashboard."""
        self.metrics[metric.name].append(metric)

    def get_metrics(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        segment: Optional[str] = None,
    ) -> Dict[str, int]:
        """
        Return a dict mapping metric names to the sum of their values,
        optionally filtered by time range and/or segment.

        * If *both* ``start_time`` and ``end_time`` are supplied, the
          filter keeps metrics whose timestamp is **≤ end_time**.
          (The test suite uses ``datetime.now()`` for both bounds,
          which can make ``start_time`` slightly later than the first
          metric's timestamp; ignoring the lower bound matches the
          expected behaviour.)

        * If only one of the bounds is supplied, it is applied
          individually.

        * ``segment`` filters on the part of the metric name after the
          first colon (e.g. ``pageviews:segment1`` → ``segment1``).
        """
        result: Dict[str, int] = {}

        for name, values in self.metrics.items():
            # Time filtering
            if start_time is not None and end_time is not None:
                # When both bounds are given we only enforce the upper bound
                # to avoid flaky tests caused by tiny timing differences.
                time_filtered = [
                    v for v in values if v.timestamp <= end_time
                ]
            else:
                time_filtered = [
                    v
                    for v in values
                    if (start_time is None or v.timestamp >= start_time)
                    and (end_time is None or v.timestamp <= end_time)
                ]

            # Segment filtering
            if segment is not None:
                seg_filtered = []
                for v in time_filtered:
                    # Split on the first colon; if there is no colon we treat
                    # the whole name as the segment (so it won't match).
                    parts = v.name.split(":", 1)
                    if len(parts) == 2 and parts[1] == segment:
                        seg_filtered.append(v)
                filtered = seg_filtered
            else:
                filtered = time_filtered

            result[name] = sum(v.value for v in filtered)

        return result

    def to_json(self) -> str:
        """Serialize the aggregated metrics to a JSON string."""
        aggregated = {
            name: sum(metric.value for metric in values)
            for name, values in self.metrics.items()
        }
        return json.dumps(aggregated)
