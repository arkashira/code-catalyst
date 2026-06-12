from mvp_builder import MVPBuilder, Component, Page
import json
import os

def test_add_page():
    builder = MVPBuilder()
    builder.add_page("Home")
    assert len(builder.layout.pages) == 1
    assert builder.layout.pages[0].name == "Home"

def test_add_component():
    builder = MVPBuilder()
    builder.add_page("Home")
    component = Component("Button", {"label": "Click me"})
    builder.add_component("Home", component)
    assert len(builder.layout.pages[0].components) == 1
    assert builder.layout.pages[0].components[0].type == "Button"

def test_reorder_components():
    builder = MVPBuilder()
    builder.add_page("Home")
    component1 = Component("Button", {"label": "Click me"})
    component2 = Component("Form", {"fields": ["name", "email"]})
    builder.add_component("Home", component1)
    builder.add_component("Home", component2)
    builder.reorder_components("Home", 0, 1)
    assert builder.layout.pages[0].components[0].type == "Form"

def test_persist():
    builder = MVPBuilder()
    builder.add_page("Home")
    component = Component("Button", {"label": "Click me"})
    builder.add_component("Home", component)
    builder.persist()
    with open("layout.json", "r") as f:
        layout = json.load(f)
    assert len(layout) == 1
    assert layout[0]["name"] == "Home"
    assert len(layout[0]["components"]) == 1
    assert layout[0]["components"][0]["type"] == "Button"
    os.remove("layout.json")

def test_preview():
    builder = MVPBuilder()
    builder.add_page("Home")
    component = Component("Button", {"label": "Click me"})
    builder.add_component("Home", component)
    builder.preview()
