import json
from dataclasses import dataclass
from datetime import datetime
import argparse

@dataclass
class Feature:
    name: str
    start_date: str
    end_date: str

class GanttChart:
    def __init__(self, features):
        self.features = features

    def update_chart(self, new_features):
        self.features = new_features

    def export_chart(self, filename):
        with open(filename, 'w') as f:
            for feature in self.features:
                f.write(f"{feature.name}: {feature.start_date} - {feature.end_date}\n")

def parse_blueprint(blueprint):
    features = []
    for feature in blueprint['features']:
        features.append(Feature(feature['name'], feature['start_date'], feature['end_date']))
    return features

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--blueprint', help='Path to blueprint JSON file')
    parser.add_argument('--output', help='Path to output PNG file')
    args = parser.parse_args()

    with open(args.blueprint, 'r') as f:
        blueprint = json.load(f)

    features = parse_blueprint(blueprint)
    chart = GanttChart(features)
    chart.export_chart(args.output)

if __name__ == '__main__':
    main()
