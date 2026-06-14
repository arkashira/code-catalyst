import json
from src.code_catalyst import generate_mvp_blueprint, store_mvp_blueprint, MVPBlueprint
import pytest
import os

def test_generate_mvp_blueprint():
    market_insight = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"]
    }
    mvp_blueprint = generate_mvp_blueprint(market_insight)
    assert isinstance(mvp_blueprint, MVPBlueprint)
    assert mvp_blueprint.core_features == market_insight["core_features"]
    assert mvp_blueprint.tech_stack == market_insight["tech_stack"]

def test_estimate_build_time():
    core_features = ["feature1", "feature2"]
    tech_stack = ["tech1", "tech2"]
    estimated_build_time = generate_mvp_blueprint({"core_features": core_features, "tech_stack": tech_stack}).estimated_build_time
    assert isinstance(estimated_build_time, str)

def test_store_mvp_blueprint(tmp_path):
    user_workspace = tmp_path / "user_workspace"
    user_workspace.mkdir()
    market_insight = {
        "core_features": ["feature1", "feature2"],
        "tech_stack": ["tech1", "tech2"]
    }
    mvp_blueprint = generate_mvp_blueprint(market_insight)
    store_mvp_blueprint(mvp_blueprint, str(user_workspace))
    assert (user_workspace / "mvp_blueprint.json").exists()
    with open(user_workspace / "mvp_blueprint.json", "r") as f:
        stored_mvp_blueprint = json.load(f)
    assert stored_mvp_blueprint["core_features"] == mvp_blueprint.core_features
    assert stored_mvp_blueprint["tech_stack"] == mvp_blueprint.tech_stack
    assert stored_mvp_blueprint["estimated_build_time"] == mvp_blueprint.estimated_build_time
