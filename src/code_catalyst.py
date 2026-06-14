import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class MVPBlueprint:
    core_features: list
    tech_stack: list
    estimated_build_time: str

def generate_mvp_blueprint(market_insight: dict) -> MVPBlueprint:
    core_features = market_insight.get("core_features", [])
    tech_stack = market_insight.get("tech_stack", [])
    estimated_build_time = estimate_build_time(core_features, tech_stack)
    return MVPBlueprint(core_features, tech_stack, estimated_build_time)

def estimate_build_time(core_features: list, tech_stack: list) -> str:
    # Simple estimation based on the number of features and tech stack complexity
    feature_complexity = len(core_features) * 2
    tech_stack_complexity = len(tech_stack) * 3
    total_complexity = feature_complexity + tech_stack_complexity
    estimated_build_time = str(timedelta(days=total_complexity))
    return estimated_build_time

def store_mvp_blueprint(mvp_blueprint: MVPBlueprint, user_workspace: str) -> None:
    with open(f"{user_workspace}/mvp_blueprint.json", "w") as f:
        json.dump({
            "core_features": mvp_blueprint.core_features,
            "tech_stack": mvp_blueprint.tech_stack,
            "estimated_build_time": mvp_blueprint.estimated_build_time
        }, f)
