import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class MVPBlueprint:
    core_features: list
    tech_stack: list
    estimated_build_time: int

def generate_mvp_blueprint(market_validation_data: Dict) -> MVPBlueprint:
    core_features = market_validation_data.get("core_features", [])
    tech_stack = market_validation_data.get("tech_stack", [])
    estimated_build_time = market_validation_data.get("estimated_build_time", 0)
    return MVPBlueprint(core_features, tech_stack, estimated_build_time)

def store_blueprint_in_workspace(blueprint: MVPBlueprint, user_id: int) -> None:
    # In-memory storage for demonstration purposes
    workspace = {}
    workspace[user_id] = blueprint
    return workspace

def validate_market_insight(market_validation_data: Dict) -> bool:
    required_fields = ["core_features", "tech_stack", "estimated_build_time"]
    return all(field in market_validation_data for field in required_fields)

def process_market_insight(market_validation_data: Dict) -> Dict:
    if not validate_market_insight(market_validation_data):
        raise ValueError("Invalid market insight data")
    blueprint = generate_mvp_blueprint(market_validation_data)
    user_id = 1  # Placeholder user ID
    store_blueprint_in_workspace(blueprint, user_id)
    return {
        "core_features": blueprint.core_features,
        "tech_stack": blueprint.tech_stack,
        "estimated_build_time": blueprint.estimated_build_time,
    }
