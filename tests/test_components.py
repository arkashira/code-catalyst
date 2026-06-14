from src.components import Component, ComponentLibrary, ApplicationBuilder
import pytest

def test_component_creation():
    component = Component("Test", "Test component", {"test": "config"})
    assert component.name == "Test"
    assert component.description == "Test component"
    assert component.config == {"test": "config"}

def test_component_library():
    library = ComponentLibrary()
    component = Component("Test", "Test component", {"test": "config"})
    library.add_component(component)
    assert len(library.get_components()) == 1

def test_application_builder():
    builder = ApplicationBuilder()
    component = Component("Test", "Test component", {"test": "config"})
    builder.add_component_to_app(component)
    assert len(builder.get_app_components()) == 1

def test_drag_and_drop_components():
    library = ComponentLibrary()
    builder = ApplicationBuilder()

    # Add components to library
    library.add_component(Component("Login", "Login functionality", {"username": "", "password": ""}))
    library.add_component(Component("Dashboard", "Dashboard view", {"title": "", "content": ""}))

    # Get components from library
    components = library.get_components()

    # Add components to application
    for component in components:
        builder.add_component_to_app(component)

    # Get application components
    app_components = builder.get_app_components()

    # Check application components
    assert len(app_components) == 2
    assert app_components[0].name == "Login"
    assert app_components[1].name == "Dashboard"
