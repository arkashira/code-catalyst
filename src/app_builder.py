from components import ComponentLibrary, Component

class AppBuilder:
    def __init__(self, library):
        self.library = library
        self.app_components = []

    def add_component(self, component_name):
        for c in self.library.get_components():
            if c.name == component_name:
                self.app_components.append(c)
                return
        raise ValueError("Component not found")

    def get_app_components(self):
        return self.app_components

    def save_app_to_json(self, filename):
        data = [{"name": c.name, "config": c.config} for c in self.app_components]
        with open(filename, "w") as f:
            import json
            json.dump(data, f)
