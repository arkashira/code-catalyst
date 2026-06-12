from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Variant:
    """A single variant of an A/B test."""

    name: str
    metrics: Dict[str, int] = field(default_factory=dict)

    def record_metric(self, metric_name: str, value: int) -> None:
        """Add *value* to the metric identified by *metric_name*."""
        if value < 0:
            raise ValueError("Metric value must be non‑negative")
        self.metrics[metric_name] = self.metrics.get(metric_name, 0) + value


@dataclass
class ABTest:
    """Container for an A/B test with multiple variants."""

    name: str
    variants: Dict[str, Variant] = field(default_factory=dict)
    active_variant: str | None = None

    def add_variant(self, variant_name: str) -> None:
        """Add a new variant to the test."""
        if variant_name in self.variants:
            raise ValueError(f"Variant '{variant_name}' already exists")
        self.variants[variant_name] = Variant(name=variant_name)
        # If this is the first variant, make it active by default
        if self.active_variant is None:
            self.active_variant = variant_name

    def set_active(self, variant_name: str) -> None:
        """Mark *variant_name* as the currently active variant."""
        if variant_name not in self.variants:
            raise KeyError(f"Variant '{variant_name}' does not exist")
        self.active_variant = variant_name

    def record_metric(self, variant_name: str, metric_name: str, value: int) -> None:
        """Record a metric for a specific variant."""
        if variant_name not in self.variants:
            raise KeyError(f"Variant '{variant_name}' does not exist")
        self.variants[variant_name].record_metric(metric_name, value)

    def get_metrics(self) -> Dict[str, Dict[str, int]]:
        """Return a deep copy of all metrics for each variant."""
        return {v_name: copy.deepcopy(v.metrics) for v_name, v in self.variants.items()}


class Dashboard:
    """High‑level manager for multiple A/B tests."""

    def __init__(self) -> None:
        self._tests: Dict[str, ABTest] = {}

    # --------------------------------------------------------------------- #
    # Test lifecycle
    # --------------------------------------------------------------------- #
    def create_test(self, test_name: str, variant_names: List[str]) -> None:
        """Create a new A/B test with the given *variant_names*."""
        if test_name in self._tests:
            raise ValueError(f"Test '{test_name}' already exists")
        if not variant_names:
            raise ValueError("At least one variant must be provided")
        test = ABTest(name=test_name)
        for v_name in variant_names:
            test.add_variant(v_name)
        self._tests[test_name] = test

    def delete_test(self, test_name: str) -> None:
        """Remove a test from the dashboard."""
        self._tests.pop(test_name, None)

    def list_tests(self) -> List[str]:
        """Return a list of all test names."""
        return list(self._tests.keys())

    def get_test(self, test_name: str) -> ABTest:
        """Retrieve the ABTest object; raises KeyError if missing."""
        if test_name not in self._tests:
            raise KeyError(f"Test '{test_name}' does not exist")
        return self._tests[test_name]

    # --------------------------------------------------------------------- #
    # Variant & metric helpers
    # --------------------------------------------------------------------- #
    def set_active_variant(self, test_name: str, variant_name: str) -> None:
        """Switch the active variant for a given test."""
        self.get_test(test_name).set_active(variant_name)

    def record_metric(
        self,
        test_name: str,
        variant_name: str,
        metric_name: str,
        value: int,
    ) -> None:
        """Record a metric for a specific test/variant."""
        self.get_test(test_name).record_metric(variant_name, metric_name, value)

    def get_results(self, test_name: str) -> Dict[str, Dict[str, int]]:
        """Return the metrics dictionary for the requested test."""
        return self.get_test(test_name).get_metrics()
