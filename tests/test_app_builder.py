from app_builder import AppBuilder
from components import ComponentLibrary, Component
import pytest

def test_app_builder():
    library = ComponentLibrary()
    component = Component("test_component", {"key": "value"})
    library.add_component(component)
    builder = AppBuilder(library)
    builder.add_component("test_component")
    assert len(builder.get_app_components()) == 1
    assert builder.get_app_components()[0].name == "test_component"
    assert builder.get_app_components()[0].config == {"key": "value"}

def test_save_app_to_json():
    library = ComponentLibrary()
    component = Component("test_component", {"key": "value"})
    library.add_component(component)
    builder = AppBuilder(library)
    builder.add_component("test_component")
    builder.save_app_to_json("app.json")
    with open("app.json", "r") as f:
        import json
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "test_component"
    assert data[0]["config"] == {"key": "value"}
