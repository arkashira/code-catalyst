import json
from dataclasses import dataclass
from typing import List

@dataclass
class Variant:
    name: str
    traffic_ratio: int

@dataclass
class Page:
    name: str
    variants: List[Variant]

class ABTesting:
    def __init__(self):
        self.pages = {}

    def add_page(self, page: Page):
        self.pages[page.name] = page

    def get_page(self, page_name: str):
        return self.pages.get(page_name)

    def split_traffic(self, page_name: str):
        page = self.get_page(page_name)
        if page:
            total_ratio = sum(variant.traffic_ratio for variant in page.variants)
            return {variant.name: variant.traffic_ratio / total_ratio for variant in page.variants}
        return {}

    def get_results(self, page_name: str):
        page = self.get_page(page_name)
        if page:
            # Simulate results for demonstration purposes
            return {variant.name: {"CTR": 0.5, "conversion": 0.2} for variant in page.variants}
        return {}
