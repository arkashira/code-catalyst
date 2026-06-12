from mvp_builder import MVPBuilder, Page, Component
import json

def test_add_page():
    builder = MVPBuilder()
    builder.add_page("Home")
    assert len(builder.pages) == 1
    assert builder.pages[0].name == "Home"

def test_add_component():
    builder = MVPBuilder()
    builder.add_page("Home")
    builder.add_component("button", 10, 20)
    assert len(builder.pages[0].components) == 1
    assert builder.pages[0].components[0].type == "button"

def test_reorder_components():
    builder = MVPBuilder()
    builder.add_page("Home")
    builder.add_component("button", 10, 20)
    builder.add_component("form", 30, 40)
    builder.reorder_components(0, 1)
    assert len(builder.pages[0].components) == 2
    assert builder.pages[0].components[0].type == "form"

def test_get_project_state():
    builder = MVPBuilder()
    builder.add_page("Home")
    builder.add_component("button", 10, 20)
    project_state = builder.get_project_state()
    expected_state = '[{"name": "Home", "components": [{"type": "button", "x": 10, "y": 20}]}]'
    assert project_state == expected_state

def test_preview():
    builder = MVPBuilder()
    builder.add_page("Home")
    builder.add_component("button", 10, 20)
    builder.preview()
