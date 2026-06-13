import pytest

from code_catalyst import IdeaWizard, InMemoryDB, Idea


@pytest.fixture
def wizard():
    return IdeaWizard()


@pytest.fixture
def db():
    return InMemoryDB()


def test_validate_success(wizard):
    payload = {
        "product_name": "  MyApp  ",
        "target_audience": "Developers",
        "core_features": ["Feature A", "Feature B"],
        "revenue_model": "Freemium",
    }
    idea = wizard.validate(payload)
    assert isinstance(idea, Idea)
    # Whitespace should be stripped
    assert idea.product_name == "MyApp"
    assert idea.core_features == ["Feature A", "Feature B"]


def test_validate_missing_fields(wizard):
    payload = {
        "product_name": "App",
        "target_audience": "Users",
        # core_features omitted
        "revenue_model": "Subscription",
    }
    with pytest.raises(ValueError) as exc:
        wizard.validate(payload)
    assert "Missing required fields" in str(exc.value)
    assert "core_features" in str(exc.value)


def test_validate_empty_string(wizard):
    payload = {
        "product_name": "   ",
        "target_audience": "Users",
        "core_features": ["Feature"],
        "revenue_model": "Ads",
    }
    with pytest.raises(ValueError) as exc:
        wizard.validate(payload)
    assert "'product_name' must be a non‑empty string." in str(exc.value)


def test_validate_core_features_edge_cases(wizard):
    # Empty list
    payload = {
        "product_name": "App",
        "target_audience": "Users",
        "core_features": [],
        "revenue_model": "Ads",
    }
    with pytest.raises(ValueError) as exc:
        wizard.validate(payload)
    assert "'core_features' must be a non‑empty list." in str(exc.value)

    # List with empty string
    payload["core_features"] = ["", "Feature"]
    with pytest.raises(ValueError) as exc:
        wizard.validate(payload)
    assert "core_features[0] must be a non‑empty string." in str(exc.value)


def test_process_submission_happy_path(wizard, db):
    payload = {
        "product_name": "App",
        "target_audience": "Users",
        "core_features": ["Feature"],
        "revenue_model": "Ads",
    }
    idea = wizard.process_submission(payload, db)
    assert isinstance(idea, Idea)
    # Ensure it was stored
    stored = db.all()
    assert len(stored) == 1
    assert stored[0] == idea


def test_process_submission_invalid_data(wizard, db):
    payload = {
        "product_name": "App",
        "target_audience": "Users",
        "core_features": [],  # invalid
        "revenue_model": "Ads",
    }
    with pytest.raises(ValueError):
        wizard.process_submission(payload, db)
    # DB must remain empty
    assert db.all() == []
