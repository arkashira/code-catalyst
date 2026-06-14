import pytest
from project import ProjectManager

def test_create_project():
    manager = ProjectManager()
    assert manager.create_project("test_project")
    assert not manager.create_project("test_project")

def test_add_page():
    manager = ProjectManager()
    manager.create_project("test_project")
    assert manager.add_page("test_project", "test_page")
    assert not manager.add_page("non_existent_project", "test_page")

def test_add_component():
    manager = ProjectManager()
    manager.create_project("test_project")
    manager.add_page("test_project", "test_page")
    assert manager.add_component("test_project", "test_page", "test_component")
    assert not manager.add_component("non_existent_project", "test_page", "test_component")
    assert not manager.add_component("test_project", "non_existent_page", "test_component")

def test_save_project():
    manager = ProjectManager()
    manager.create_project("test_project")
    manager.add_page("test_project", "test_page")
    manager.add_component("test_project", "test_page", "test_component")
    assert manager.save_project("test_project")
    assert not manager.save_project("non_existent_project")
