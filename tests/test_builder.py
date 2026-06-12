from builder import Builder, Component, Page
import json

def test_add_page():
    builder = Builder()
    page = Page([Component("text", "Hello World")])
    builder.add_page(page)
    assert len(builder.pages) == 1

def test_export_schema():
    builder = Builder()
    page = Page([Component("text", "Hello World"), Component("input", "", "username")])
    builder.add_page(page)
    schema = builder.export_schema()
    assert json.loads(schema) == [[{"type": "text", "text": "Hello World", "name": ""}, {"type": "input", "text": "", "name": "username"}]]

def test_add_component():
    builder = Builder()
    page = Page([Component("text", "Hello World")])
    builder.add_page(page)
    builder.add_component(0, Component("input", "", "username"))
    assert len(builder.pages[0].components) == 2

def test_remove_component():
    builder = Builder()
    page = Page([Component("text", "Hello World"), Component("input", "", "username")])
    builder.add_page(page)
    builder.remove_component(0, 0)
    assert len(builder.pages[0].components) == 1

def test_update_component():
    builder = Builder()
    page = Page([Component("text", "Hello World")])
    builder.add_page(page)
    builder.update_component(0, 0, Component("text", "New Text"))
    assert builder.pages[0].components[0].text == "New Text"
