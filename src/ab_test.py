import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Variant:
    url: str
    clicks: int = 0
    conversions: int = 0

class ABTest:
    def __init__(self, variant1: Variant, variant2: Variant):
        self.variant1 = variant1
        self.variant2 = variant2
        self.total_clicks = 0
        self.total_conversions = 0

    def split_traffic(self):
        return self.variant1, self.variant2

    def update_results(self, variant: Variant, clicked: bool, converted: bool):
        if clicked:
            variant.clicks += 1
            self.total_clicks += 1
        if converted:
            variant.conversions += 1
            self.total_conversions += 1

    def get_results(self):
        return {
            'variant1': {
                'url': self.variant1.url,
                'clicks': self.variant1.clicks,
                'conversions': self.variant1.conversions,
                'ctr': self.variant1.clicks / (self.variant1.clicks + self.variant2.clicks) if self.total_clicks > 0 else 0,
                'conversion_rate': self.variant1.conversions / self.variant1.clicks if self.variant1.clicks > 0 else 0
            },
            'variant2': {
                'url': self.variant2.url,
                'clicks': self.variant2.clicks,
                'conversions': self.variant2.conversions,
                'ctr': self.variant2.clicks / (self.variant1.clicks + self.variant2.clicks) if self.total_clicks > 0 else 0,
                'conversion_rate': self.variant2.conversions / self.variant2.clicks if self.variant2.clicks > 0 else 0
            }
        }

def main():
    variant1 = Variant('https://example.com/variant1')
    variant2 = Variant('https://example.com/variant2')
    ab_test = ABTest(variant1, variant2)
    print(ab_test.split_traffic())
    ab_test.update_results(variant1, True, True)
    ab_test.update_results(variant2, True, False)
    print(json.dumps(ab_test.get_results(), indent=4))

if __name__ == '__main__':
    main()
