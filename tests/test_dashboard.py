import pytest

from dashboard import Dashboard, ABTest, Variant


def test_create_and_manage_test():
    db = Dashboard()
    db.create_test("button_color", ["red", "blue"])

    # Verify test exists
    assert "button_color" in db.list_tests()

    test = db.get_test("button_color")
    assert isinstance(test, ABTest)
    # Verify variants are correctly added
    assert set(test.variants.keys()) == {"red", "blue"}
    # Active variant should default to the first added ("red")
    assert test.active_variant == "red"


def test_switch_active_variant():
    db = Dashboard()
    db.create_test("headline", ["A", "B"])
    db.set_active_variant("headline", "B")
    test = db.get_test("headline")
    assert test.active_variant == "B"

    # Switching to a non‑existent variant should raise
    with pytest.raises(KeyError):
        db.set_active_variant("headline", "C")


def test_record_and_retrieve_metrics():
    db = Dashboard()
    db.create_test("cta_text", ["short", "long"])

    # Record some engagement numbers
    db.record_metric("cta_text", "short", "clicks", 15)
    db.record_metric("cta_text", "short", "signups", 3)
    db.record_metric("cta_text", "long", "clicks", 30)

    results = db.get_results("cta_text")
    expected = {
        "short": {"clicks": 15, "signups": 3},
        "long": {"clicks": 30},
    }
    assert results == expected

    # Adding more to an existing metric should accumulate
    db.record_metric("cta_text", "short", "clicks", 5)
    results = db.get_results("cta_text")
    assert results["short"]["clicks"] == 20


def test_error_conditions():
    db = Dashboard()
    # Duplicate test creation
    db.create_test("landing", ["v1"])
    with pytest.raises(ValueError):
        db.create_test("landing", ["v2"])

    # Creating a test without variants
    with pytest.raises(ValueError):
        db.create_test("empty", [])

    # Recording metric for unknown test
    with pytest.raises(KeyError):
        db.record_metric("nonexistent", "any", "clicks", 1)

    # Recording metric for unknown variant
    db.create_test("promo", ["old"])
    with pytest.raises(KeyError):
        db.record_metric("promo", "new", "clicks", 1)

    # Negative metric value
    with pytest.raises(ValueError):
        db.record_metric("promo", "old", "clicks", -5)


def test_variant_object_direct_usage():
    # Ensure Variant behaves as expected when used directly
    v = Variant(name="test")
    v.record_metric("views", 100)
    v.record_metric("views", 50)
    assert v.metrics["views"] == 150

    with pytest.raises(ValueError):
        v.record_metric("views", -10)
