import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Component:
    type: str
    x: int
    y: int

@dataclass
class Page:
    name: str
    components: List[Component]

class MVPBuilder:
    def __init__(self):
        self.pages = []
        self.current_page = None

    def add_page(self, name):
        self.pages.append(Page(name, []))
        self.current_page = self.pages[-1]

    def add_component(self, component_type, x, y):
        if self.current_page:
            self.current_page.components.append(Component(component_type, x, y))

    def reorder_components(self, component_index, new_index):
        if self.current_page:
            component = self.current_page.components.pop(component_index)
            self.current_page.components.insert(new_index, component)

    def get_project_state(self):
        return json.dumps([asdict(page) for page in self.pages])

    def preview(self):
        # Simulate previewing the project state
        print("Previewing project state:")
        print(self.get_project_state())
