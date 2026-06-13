import pytest
from code_catalyst import CodeCatalyst, Component

def test_add_component():
    catalyst = CodeCatalyst()
    catalyst.add_component("auth")
    assert len(catalyst.components) == 1
    assert catalyst.components[0].name == "auth"

def test_add_component_not_in_library():
    catalyst = CodeCatalyst()
    with pytest.raises(ValueError):
        catalyst.add_component("unknown")

def test_customize_component():
    catalyst = CodeCatalyst()
    catalyst.add_component("auth")
    catalyst.customize_component("auth", {"type": "custom"})
    assert catalyst.components[0].config == {"type": "custom"}

def test_customize_component_not_in_application():
    catalyst = CodeCatalyst()
    with pytest.raises(ValueError):
        catalyst.customize_component("auth", {"type": "custom"})

def test_get_application_config():
    catalyst = CodeCatalyst()
    catalyst.add_component("auth")
    catalyst.add_component("payment")
    config = catalyst.get_application_config()
    assert config == {"auth": {"type": "oauth"}, "payment": {"type": "stripe"}}

def test_get_library():
    catalyst = CodeCatalyst()
    library = catalyst.get_library()
    assert library == {"auth": {"type": "oauth"}, "payment": {"type": "stripe"}, "database": {"type": "mysql"}}
