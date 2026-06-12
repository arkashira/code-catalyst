import json
import os
import random
import statistics
from dataclasses import dataclass, field
from typing import Dict

DATA_FILE = "dashboard.json"

@dataclass
class Variation:
    name: str
    impressions: int = 0
    conversions: int = 0

    def conversion_rate(self) -> float:
        return self.conversions / self.impressions if self.impressions else 0.0

@dataclass
class ABTest:
    name: str
    variations: Dict[str, Variation] = field(default_factory=dict)
    running: bool = False

    def add_variation(self, name: str):
        if len(self.variations) >= 3:
            raise ValueError("Maximum 3 variations allowed")
        if name in self.variations:
            raise ValueError(f"Variation {name} already exists")
        self.variations[name] = Variation(name)

    def start(self):
        if self.running:
            raise RuntimeError("Test already running")
        self.running = True

    def stop(self):
        if not self.running:
            raise RuntimeError("Test not running")
        self.running = False
        self._update_dashboard()

    def record_impression(self, variation_name: str, converted: bool):
        if not self.running:
            raise RuntimeError("Test not running")
        var = self.variations.get(variation_name)
        if not var:
            raise ValueError(f"Unknown variation {variation_name}")
        var.impressions += 1
        if converted:
            var.conversions += 1

    def _p_value(self, var1: Variation, var2: Variation) -> float:
        # Two-proportion z-test
        n1, n2 = var1.impressions, var2.impressions
        if n1 == 0 or n2 == 0:
            return 1.0
        p1, p2 = var1.conversion_rate(), var2.conversion_rate()
        p_pool = (var1.conversions + var2.conversions) / (n1 + n2)
        se = (p_pool * (1 - p_pool) * (1 / n1 + 1 / n2)) ** 0.5
        if se == 0:
            return 1.0
        z = abs(p1 - p2) / se
        # two-tailed
        p_value = 2 * (1 - statistics.NormalDist().cdf(z))
        return p_value

    def results(self) -> Dict[str, Dict]:
        res = {}
        names = list(self.variations.keys())
        for i, name in enumerate(names):
            var = self.variations[name]
            res[name] = {
                "impressions": var.impressions,
                "conversions": var.conversions,
                "conversion_rate": var.conversion_rate(),
            }
            if i > 0:
                p = self._p_value(var, self.variations[names[0]])
                res[name]["p_value_vs_control"] = p
                res[name]["significant_vs_control"] = p < 0.05
        return res

    def _update_dashboard(self):
        dashboard = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                dashboard = json.load(f)
        dashboard[self.name] = self.results()
        with open(DATA_FILE, "w") as f:
            json.dump(dashboard, f, indent=2)
