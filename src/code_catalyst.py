import json
from dataclasses import dataclass
from typing import List

@dataclass
class PageTemplate:
    name: str
    components: List[str]

@dataclass
class Component:
    name: str
    position: int

class CodeCatalyst:
    def __init__(self):
        self.page_templates = [
            PageTemplate("Home", ["Header", "Footer"]),
            PageTemplate("About", ["Header", "Content", "Footer"]),
            PageTemplate("Contact", ["Header", "Form", "Footer"]),
            PageTemplate("Blog", ["Header", "Posts", "Footer"]),
            PageTemplate("FAQ", ["Header", "Questions", "Footer"]),
        ]
        self.components = []
        self.changes = []

    def add_page_template(self, name: str, components: List[str]):
        self.page_templates.append(PageTemplate(name, components))
        self.changes.append({"action": "add_page_template", "name": name, "components": components})

    def add_component(self, name: str, position: int):
        self.components.append(Component(name, position))
        self.changes.append({"action": "add_component", "name": name, "position": position})

    def reposition_component(self, name: str, new_position: int):
        for component in self.components:
            if component.name == name:
                component.position = new_position
                self.changes.append({"action": "reposition_component", "name": name, "new_position": new_position})
                break

    def autosave(self):
        with open("autosave.json", "w") as f:
            json.dump({"page_templates": [pt.__dict__ for pt in self.page_templates], "components": [c.__dict__ for c in self.components], "changes": self.changes}, f)

    def version(self):
        return len(self.changes)
