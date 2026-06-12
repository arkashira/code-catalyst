import json
from typing import Dict, List

def load_config(path: str) -> Dict[str, List[Dict]]:
    """
    Load A/B test configuration from a JSON file.
    Expected format:
    {
        "feature_name": [
            {"name": "A", "weight": 0.5},
            {"name": "B", "weight": 0.5}
        ],
        ...
    }
    """
    with open(path, "r") as f:
        return json.load(f)

def save_results(path: str, results: List[Dict]):
    """
    Persist results to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
