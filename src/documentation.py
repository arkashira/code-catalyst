import json
from dataclasses import dataclass
from typing import List

@dataclass
class Resource:
    title: str
    content: str

class Documentation:
    def __init__(self):
        self.resources = []

    def add_resource(self, resource: Resource):
        self.resources.append(resource)

    def get_resources(self):
        return self.resources

    def save_to_json(self, filename: str):
        data = [{"title": resource.title, "content": resource.content} for resource in self.resources]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_json(self, filename: str):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.resources = [Resource(resource["title"], resource["content"]) for resource in data]
        except FileNotFoundError:
            pass

class SupportResources:
    def __init__(self):
        self.documentation = Documentation()

    def add_documentation_resource(self, title: str, content: str):
        self.documentation.add_resource(Resource(title, content))

    def get_documentation_resources(self):
        return self.documentation.get_resources()

    def save_documentation_to_json(self, filename: str):
        self.documentation.save_to_json(filename)

    def load_documentation_from_json(self, filename: str):
        self.documentation.load_from_json(filename)
