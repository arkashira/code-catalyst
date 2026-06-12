import json
from dataclasses import dataclass
from typing import List

@dataclass
class Version:
    name: str
    parameters: dict

@dataclass
class Test:
    name: str
    versions: List[Version]
    target_audience: str
    results: dict

class ABTesting:
    def __init__(self):
        self.tests = []

    def create_version(self, name, parameters):
        return Version(name, parameters)

    def create_test(self, name, versions, target_audience):
        test = Test(name, versions, target_audience, {})
        self.tests.append(test)
        return test

    def run_test(self, test):
        # Simulate running the test
        test.results = {
            test.versions[0].name: 50,
            test.versions[1].name: 50
        }

    def view_results(self, test):
        return test.results

    def compare_results(self, test):
        version1, version2 = test.versions
        results = test.results
        if results[version1.name] > results[version2.name]:
            return f"{version1.name} performs better"
        elif results[version1.name] < results[version2.name]:
            return f"{version2.name} performs better"
        else:
            return "Both versions perform equally"
