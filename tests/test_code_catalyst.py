import pytest
import json
from code_catalyst import CodeCatalyst, PageTemplate, Component

def test_add_page_template():
    cc = CodeCatalyst()
    cc.add_page_template("Test", ["Header", "Footer"])
    assert len(cc.page_templates) == 6
    assert cc.page_templates[-1].name == "Test"
    assert cc.page_templates[-1].components == ["Header", "Footer"]

def test_add_component():
    cc = CodeCatalyst()
    cc.add_component("Test", 0)
    assert len(cc.components) == 1
    assert cc.components[0].name == "Test"
    assert cc.components[0].position == 0

def test_reposition_component():
    cc = CodeCatalyst()
    cc.add_component("Test", 0)
    cc.reposition_component("Test", 1)
    assert cc.components[0].position == 1

def test_autosave():
    cc = CodeCatalyst()
    cc.add_page_template("Test", ["Header", "Footer"])
    cc.add_component("Test", 0)
    cc.autosave()
    with open("autosave.json", "r") as f:
        data = json.load(f)
    assert len(data["page_templates"]) == 6
    assert data["page_templates"][-1]["name"] == "Test"
    assert len(data["components"]) == 1
    assert data["components"][0]["name"] == "Test"

def test_version():
    cc = CodeCatalyst()
    cc.add_page_template("Test", ["Header", "Footer"])
    cc.add_component("Test", 0)
    assert cc.version() == 2
