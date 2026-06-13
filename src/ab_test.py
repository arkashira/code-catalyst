import json
from dataclasses import dataclass
from random import random

@dataclass
class Variant:
    name: str
    traffic_percentage: float

class ABTest:
    def __init__(self, variant1, variant2):
        self.variant1 = variant1
        self.variant2 = variant2
        self.results = {variant1.name: 0, variant2.name: 0}

    def split_traffic(self):
        if random() < self.variant1.traffic_percentage / 100:
            return self.variant1.name
        else:
            return self.variant2.name

    def record_engagement(self, variant_name):
        self.results[variant_name] += 1

    def get_results(self):
        return self.results

    def get_statistical_significance(self):
        # Simple statistical significance calculation for demonstration purposes
        total_engagements = sum(self.results.values())
        if total_engagements == 0:
            return 0
        variant1_engagements = self.results[self.variant1.name]
        variant2_engagements = self.results[self.variant2.name]
        variant1_percentage = variant1_engagements / total_engagements
        variant2_percentage = variant2_engagements / total_engagements
        if abs(variant1_percentage - variant2_percentage) > 0.1:
            return "Statistically significant difference"
        else:
            return "No statistically significant difference"
