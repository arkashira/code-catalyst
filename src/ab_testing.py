import json
from dataclasses import dataclass
from typing import Dict, List

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

    def split_traffic(self, page_name: str):
        page = self.pages.get(page_name)
        if page:
            total_ratio = sum(variant.traffic_ratio for variant in page.variants)
            traffic_split = {variant.name: variant.traffic_ratio / total_ratio for variant in page.variants}
            return traffic_split
        return None

    def display_results(self, page_name: str, results: Dict[str, Dict[str, int]]):
        page = self.pages.get(page_name)
        if page:
            print(f"Results for page {page_name}:")
            for variant in page.variants:
                ctr = results.get(variant.name, {}).get("CTR", 0)
                conversion = results.get(variant.name, {}).get("conversion", 0)
                print(f"Variant {variant.name}: CTR={ctr}, conversion={conversion}")
        else:
            print("Page not found")

def main():
    ab_testing = ABTesting()
    page = Page("example", [Variant("A", 1), Variant("B", 1), Variant("C", 1)])
    ab_testing.add_page(page)
    traffic_split = ab_testing.split_traffic("example")
    print("Traffic split:", traffic_split)
    results = {
        "A": {"CTR": 10, "conversion": 5},
        "B": {"CTR": 15, "conversion": 10},
        "C": {"CTR": 8, "conversion": 3}
    }
    ab_testing.display_results("example", results)

if __name__ == "__main__":
    main()
