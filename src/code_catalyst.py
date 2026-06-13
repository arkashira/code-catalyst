import json
from dataclasses import dataclass
from typing import List

@dataclass
class Component:
    name: str
    config: dict

class CodeCatalyst:
    def __init__(self):
        self.components = []
        self.library = {
            "auth": Component("auth", {"type": "oauth"}),
            "payment": Component("payment", {"type": "stripe"}),
            "database": Component("database", {"type": "mysql"})
        }

    def add_component(self, component_name: str):
        if component_name in self.library:
            self.components.append(self.library[component_name])
        else:
            raise ValueError("Component not found in library")

    def customize_component(self, component_name: str, config: dict):
        for component in self.components:
            if component.name == component_name:
                component.config = config
                break
        else:
            raise ValueError("Component not found in application")

    def get_application_config(self):
        return {component.name: component.config for component in self.components}

    def get_library(self):
        return {name: component.config for name, component in self.library.items()}
