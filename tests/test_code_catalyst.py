import json
from src.code_catalyst import process_market_insight, MVPBlueprint

def test_generate_mvp_blueprint():
    market_validation_data = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"],
        "estimated_build_time": 10,
    }
    blueprint = MVPBlueprint(**market_validation_data)
    assert blueprint.core_features == market_validation_data["core_features"]
    assert blueprint.tech_stack == market_validation_data["tech_stack"]
    assert blueprint.estimated_build_time == market_validation_data["estimated_build_time"]

def test_store_blueprint_in_workspace():
    blueprint = MVPBlueprint(["feature1", "feature2"], ["tech1", "tech2"], 10)
    user_id = 1
    workspace = {}
    workspace[user_id] = blueprint
    assert workspace[user_id].core_features == blueprint.core_features
    assert workspace[user_id].tech_stack == blueprint.tech_stack
    assert workspace[user_id].estimated_build_time == blueprint.estimated_build_time

def test_validate_market_insight():
    market_validation_data = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"],
        "estimated_build_time": 10,
    }
    assert process_market_insight(market_validation_data) is not None

def test_process_market_insight_invalid_data():
    market_validation_data = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"],
    }
    try:
        process_market_insight(market_validation_data)
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "Invalid market insight data"

def test_process_market_insight():
    market_validation_data = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"],
        "estimated_build_time": 10,
    }
    result = process_market_insight(market_validation_data)
    assert result["core_features"] == market_validation_data["core_features"]
    assert result["tech_stack"] == market_validation_data["tech_stack"]
    assert result["estimated_build_time"] == market_validation_data["estimated_build_time"]
