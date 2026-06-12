import json
from dataclasses import dataclass
from typing import List

@dataclass
class Component:
    type: str
    text: str = ""
    name: str = ""

@dataclass
class Page:
    components: List[Component]

class Builder:
    def __init__(self):
        self.pages = []

    def add_page(self, page: Page):
        self.pages.append(page)

    def export_schema(self):
        schema = []
        for page in self.pages:
            page_schema = []
            for component in page.components:
                component_schema = {
                    "type": component.type,
                    "text": component.text,
                    "name": component.name
                }
                page_schema.append(component_schema)
            schema.append(page_schema)
        return json.dumps(schema)

    def add_component(self, page_index: int, component: Component):
        if page_index < len(self.pages):
            self.pages[page_index].components.append(component)

    def remove_component(self, page_index: int, component_index: int):
        if page_index < len(self.pages) and component_index < len(self.pages[page_index].components):
            del self.pages[page_index].components[component_index]

    def update_component(self, page_index: int, component_index: int, component: Component):
        if page_index < len(self.pages) and component_index < len(self.pages[page_index].components):
            self.pages[page_index].components[component_index] = component
