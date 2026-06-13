import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Page:
    name: str
    components: list

@dataclass
class Project:
    name: str
    pages: list

class ProjectManager:
    def __init__(self):
        self.projects = {}

    def create_project(self, name):
        if name in self.projects:
            raise ValueError("Project already exists")
        self.projects[name] = Project(name, [])
        return self.projects[name]

    def add_page(self, project_name, page_name):
        if project_name not in self.projects:
            raise ValueError("Project does not exist")
        project = self.projects[project_name]
        project.pages.append(Page(page_name, []))
        return project.pages[-1]

    def add_component(self, project_name, page_name, component):
        if project_name not in self.projects:
            raise ValueError("Project does not exist")
        project = self.projects[project_name]
        for page in project.pages:
            if page.name == page_name:
                page.components.append(component)
                return page
        raise ValueError("Page does not exist")
