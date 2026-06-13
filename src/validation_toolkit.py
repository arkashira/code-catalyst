import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class FeatureUsage:
    feature_name: str
    usage_count: int

@dataclass
class ConversionFunnel:
    step_name: str
    conversion_rate: float

@dataclass
class ValidationReport:
    dau: int
    mau: int
    feature_usage: List[FeatureUsage]
    conversion_funnels: List[ConversionFunnel]

class ValidationToolkit:
    def __init__(self):
        self.usage_data = {}
        self.feature_usage = {}
        self.conversion_funnels = {}

    def track_usage(self, feature_name: str):
        if feature_name not in self.feature_usage:
            self.feature_usage[feature_name] = 0
        self.feature_usage[feature_name] += 1

    def track_conversion(self, step_name: str, conversion_rate: float):
        if step_name not in self.conversion_funnels:
            self.conversion_funnels[step_name] = []
        self.conversion_funnels[step_name].append(conversion_rate)

    def generate_report(self) -> ValidationReport:
        dau = len(self.usage_data)
        mau = len(set([datetime.strptime(date, '%Y-%m-%d').month for date in self.usage_data]))
        feature_usage = [FeatureUsage(feature, usage) for feature, usage in self.feature_usage.items()]
        conversion_funnels = [ConversionFunnel(step, sum(conversions) / len(conversions)) for step, conversions in self.conversion_funnels.items()]
        return ValidationReport(dau, mau, feature_usage, conversion_funnels)

    def ab_test(self, feature_name: str, variants: List[str]):
        if feature_name not in self.usage_data:
            self.usage_data[feature_name] = {}
        for variant in variants:
            if variant not in self.usage_data[feature_name]:
                self.usage_data[feature_name][variant] = 0
            self.usage_data[feature_name][variant] += 1

    def export_report(self, report: ValidationReport):
        report_data = {
            'dau': report.dau,
            'mau': report.mau,
            'feature_usage': [{'feature_name': feature.feature_name, 'usage_count': feature.usage_count} for feature in report.feature_usage],
            'conversion_funnels': [{'step_name': funnel.step_name, 'conversion_rate': funnel.conversion_rate} for funnel in report.conversion_funnels]
        }
        return json.dumps(report_data)
