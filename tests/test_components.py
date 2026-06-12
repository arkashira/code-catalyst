from components import Component, ComponentLibrary, ApplicationBuilder
import pytest

def test_component_creation():
    component = Component('Test', 'Test component', {'test': 'string'})
    assert component.name == 'Test'
    assert component.description == 'Test component'
    assert component.config == {'test': 'string'}

def test_component_library():
    library = ComponentLibrary()
    component = Component('Test', 'Test component', {'test': 'string'})
    library.add_component(component)
    assert len(library.get_components()) == 1
    assert library.get_components()[0].name == 'Test'

def test_application_builder():
    builder = ApplicationBuilder()
    component = Component('Test', 'Test component', {'test': 'string'})
    builder.add_component(component)
    assert len(builder.build_application()) == 1
    assert builder.build_application()[0].name == 'Test'

def test_main_list_components(capsys):
    import sys
    sys.argv = ['main.py', '--list-components']
    from src.main import main
    main()
    captured = capsys.readouterr()
    assert 'Available components:' in captured.out

def test_main_build_app(capsys):
    import sys
    sys.argv = ['main.py', '--build-app']
    from src.main import main
    main()
    captured = capsys.readouterr()
    assert 'Application built with components:' in captured.out
