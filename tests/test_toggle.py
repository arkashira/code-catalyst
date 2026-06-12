import pytest
from toggle import ToggleManager, ABTestConfig, Variant

def test_add_and_get_variant():
    manager = ToggleManager()
    config = ABTestConfig(
        feature_name="new_button",
        variants=[
            Variant(name="A", weight=0.7),
            Variant(name="B", weight=0.3),
        ],
    )
    manager.add_test(config)

    # Assign same user twice returns same variant
    v1 = manager.get_variant("user1", "new_button")
    v2 = manager.get_variant("user1", "new_button")
    assert v1 == v2

    # Different users can get different variants
    v3 = manager.get_variant("user2", "new_button")
    assert v3 in ("A", "B")

def test_invalid_feature():
    manager = ToggleManager()
    with pytest.raises(KeyError):
        manager.get_variant("user1", "unknown_feature")
