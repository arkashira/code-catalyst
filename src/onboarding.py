import json
from dataclasses import dataclass
from typing import List

@dataclass
class Feature:
    name: str
    description: str

class OnboardingProcess:
    def __init__(self):
        self.features = [
            Feature("Dashboard", "Overview of the platform"),
            Feature("Settings", "Configure your account"),
            Feature("Support", "Get help when you need it"),
        ]

    def start_onboarding(self):
        print("Welcome to the onboarding process!")
        for feature in self.features:
            print(f"Feature: {feature.name} - {feature.description}")
            input("Press Enter to continue...")
        print("Onboarding complete!")

    def get_features(self):
        return self.features

    def get_feature_by_name(self, name: str):
        for feature in self.features:
            if feature.name == name:
                return feature
        return None
