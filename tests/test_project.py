import pytest
from project import ProjectManager, Project, Page

def test_create_project():
    manager = ProjectManager()
    project = manager.create_project("My Project")
    assert project.name == "My Project"
    assert len(project.pages) == 0

def test_create_project_duplicate():
    manager = ProjectManager()
    manager.create_project("My Project")
    with pytest.raises(ValueError):
        manager.create_project("My Project")

def test_add_page():
    manager = ProjectManager()
    project = manager.create_project("My Project")
    page = manager.add_page("My Project", "My Page")
    assert page.name == "My Page"
    assert len(page.components) == 0

def test_add_page_non_existent_project():
    manager = ProjectManager()
    with pytest.raises(ValueError):
        manager.add_page("My Project", "My Page")

def test_add_component():
    manager = ProjectManager()
    project = manager.create_project("My Project")
    page = manager.add_page("My Project", "My Page")
    component = "My Component"
    updated_page = manager.add_component("My Project", "My Page", component)
    assert updated_page.name == "My Page"
    assert len(updated_page.components) == 1
    assert updated_page.components[0] == component

def test_add_component_non_existent_project():
    manager = ProjectManager()
    with pytest.raises(ValueError):
        manager.add_component("My Project", "My Page", "My Component")

def test_add_component_non_existent_page():
    manager = ProjectManager()
    project = manager.create_project("My Project")
    with pytest.raises(ValueError):
        manager.add_component("My Project", "My Page", "My Component")
