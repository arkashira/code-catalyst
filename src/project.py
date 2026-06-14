import json
from dataclasses import dataclass
from datetime import datetime, timedelta

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
            return False
        self.projects[name] = Project(name, [])
        return True

    def add_page(self, project_name, page_name):
        if project_name not in self.projects:
            return False
        project = self.projects[project_name]
        project.pages.append(Page(page_name, []))
        return True

    def add_component(self, project_name, page_name, component):
        if project_name not in self.projects:
            return False
        project = self.projects[project_name]
        for page in project.pages:
            if page.name == page_name:
                page.components.append(component)
                return True
        return False

    def save_project(self, project_name):
        if project_name not in self.projects:
            return False
        project = self.projects[project_name]
        with open(f"{project_name}.json", "w") as f:
            json.dump({
                "name": project.name,
                "pages": [{"name": page.name, "components": page.components} for page in project.pages]
            }, f)
        return True
