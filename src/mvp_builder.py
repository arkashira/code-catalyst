import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Component:
    """Represents a component that can be added to a page."""
    type: str
    data: dict = field(default_factory=dict)

@dataclass
class Page:
    """Represents a page in the MVP layout."""
    name: str
    components: List[Component] = field(default_factory=list)

@dataclass
class MVPLayout:
    """Represents the MVP layout."""
    pages: List[Page] = field(default_factory=list)

class MVPBuilder:
    """Provides a drag-and-drop interface to add pages and components."""
    def __init__(self):
        self.layout = MVPLayout()

    def add_page(self, name: str):
        """Adds a new page to the layout."""
        self.layout.pages.append(Page(name))

    def add_component(self, page_name: str, component: Component):
        """Adds a component to a page."""
        for page in self.layout.pages:
            if page.name == page_name:
                page.components.append(component)
                return
        raise ValueError("Page not found")

    def reorder_components(self, page_name: str, component_index: int, new_index: int):
        """Reorders components on a page."""
        for page in self.layout.pages:
            if page.name == page_name:
                if 0 <= new_index < len(page.components):
                    component = page.components.pop(component_index)
                    page.components.insert(new_index, component)
                    return
                raise ValueError("Invalid new index")
        raise ValueError("Page not found")

    def persist(self):
        """Persists the layout to a JSON file."""
        with open("layout.json", "w") as f:
            json.dump([{"name": page.name, "components": [{"type": component.type, "data": component.data} for component in page.components]} for page in self.layout.pages], f)

    def preview(self):
        """Previews the layout."""
        print("Previewing layout:")
        for page in self.layout.pages:
            print(f"Page: {page.name}")
            for component in page.components:
                print(f"  Component: {component.type}")
