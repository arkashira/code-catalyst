import random
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Variant:
    name: str
    weight: float  # traffic split weight (0-1)

@dataclass
class ABTestConfig:
    feature_name: str
    variants: List[Variant] = field(default_factory=list)

    def total_weight(self) -> float:
        return sum(v.weight for v in self.variants)

    def normalize(self):
        total = self.total_weight()
        if total == 0:
            raise ValueError("Total weight cannot be zero")
        for v in self.variants:
            v.weight /= total

class ToggleManager:
    """
    Simple in-memory feature toggle and A/B test manager.
    """
    def __init__(self):
        self.tests: Dict[str, ABTestConfig] = {}
        self.assignments: Dict[Tuple[str, str], str] = {}  # (user_id, feature) -> variant_name

    def add_test(self, config: ABTestConfig):
        config.normalize()
        self.tests[config.feature_name] = config

    def get_variant(self, user_id: str, feature_name: str) -> str:
        key = (user_id, feature_name)
        if key in self.assignments:
            return self.assignments[key]
        if feature_name not in self.tests:
            raise KeyError(f"No test configured for feature '{feature_name}'")
        config = self.tests[feature_name]
        rnd = random.random()
        cumulative = 0.0
        for variant in config.variants:
            cumulative += variant.weight
            if rnd < cumulative:
                self.assignments[key] = variant.name
                return variant.name
        # Fallback
        variant_name = config.variants[-1].name
        self.assignments[key] = variant_name
        return variant_name
