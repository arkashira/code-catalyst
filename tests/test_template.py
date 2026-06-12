from template import Template, TemplateEditor
import json
import os
import pytest

def test_edit_text():
    template = Template("Hello World", "logo.png", {"asset1": "asset1.png"})
    editor = TemplateEditor(template)
    editor.edit_text("New Text")
    assert editor.template.text == "New Text"

def test_upload_logo():
    template = Template("Hello World", "logo.png", {"asset1": "asset1.png"})
    editor = TemplateEditor(template)
    editor.upload_logo("new_logo.png")
    assert editor.template.logo == "new_logo.png"

def test_upload_brand_assets():
    template = Template("Hello World", "logo.png", {"asset1": "asset1.png"})
    editor = TemplateEditor(template)
    editor.upload_brand_assets({"asset2": "asset2.png"})
    assert editor.template.brand_assets == {"asset2": "asset2.png"}

def test_save_and_load():
    template = Template("Hello World", "logo.png", {"asset1": "asset1.png"})
    editor = TemplateEditor(template)
    editor.save("template.json")
    loaded_editor = TemplateEditor.load("template.json")
    assert loaded_editor.template.text == "Hello World"
    assert loaded_editor.template.logo == "logo.png"
    assert loaded_editor.template.brand_assets == {"asset1": "asset1.png"}
    os.remove("template.json")

def test_preview():
    template = Template("Hello World", "logo.png", {"asset1": "asset1.png"})
    editor = TemplateEditor(template)
    # Just test that preview doesn't throw an error
    editor.preview()
