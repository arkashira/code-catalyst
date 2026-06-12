import json
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Feedback:
    prototype_id: str
    user_id: str
    comment: str

class Prototype:
    def __init__(self, id: str, url: str):
        self.id = id
        self.url = url
        self.feedback = []

    def add_feedback(self, feedback: Feedback):
        self.feedback.append(feedback)

    def get_feedback(self):
        return self.feedback

class PrototypeManager:
    def __init__(self):
        self.prototypes = {}

    def create_prototype(self, id: str, url: str):
        self.prototypes[id] = Prototype(id, url)

    def get_prototype(self, id: str):
        if id not in self.prototypes:
            raise ValueError("Prototype not found")
        return self.prototypes[id]

    def share_prototype(self, id: str):
        prototype = self.get_prototype(id)
        return prototype.url

    def collect_feedback(self, id: str, user_id: str, comment: str):
        prototype = self.get_prototype(id)
        feedback = Feedback(id, user_id, comment)
        prototype.add_feedback(feedback)

    def view_feedback(self, id: str):
        prototype = self.get_prototype(id)
        return prototype.get_feedback()
