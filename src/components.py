from dataclasses import dataclass
from typing import List

@dataclass
class Component:
    name: str
    description: str
    config: dict

class ComponentLibrary:
    def __init__(self):
        self.components = []

    def add_component(self, component: Component):
        self.components.append(component)

    def get_components(self) -> List[Component]:
        return self.components

class ApplicationBuilder:
    def __init__(self):
        self.library = ComponentLibrary()
        self.app_components = []

    def add_component_to_app(self, component: Component):
        self.app_components.append(component)

    def get_app_components(self) -> List[Component]:
        return self.app_components
