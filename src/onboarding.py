import json
from dataclasses import dataclass
from typing import List

@dataclass
class OnboardingStep:
    description: str
    completed: bool = False

class OnboardingProcess:
    def __init__(self):
        self.steps = [
            OnboardingStep("Introduction to ProtoLaunch"),
            OnboardingStep("Key Features"),
            OnboardingStep("Workflows"),
            OnboardingStep("Creating an MVP")
        ]

    def skip_step(self, step_index: int):
        if step_index < len(self.steps):
            self.steps[step_index].completed = True

    def complete_step(self, step_index: int):
        if step_index < len(self.steps):
            self.steps[step_index].completed = True

    def is_onboarding_completed(self):
        return all(step.completed for step in self.steps)

    def get_next_step(self):
        for i, step in enumerate(self.steps):
            if not step.completed:
                return i
        return None

    def to_json(self):
        return json.dumps([{"description": step.description, "completed": step.completed} for step in self.steps])

    @classmethod
    def from_json(cls, json_str):
        onboarding_process = cls()
        steps = json.loads(json_str)
        for i, step in enumerate(steps):
            onboarding_process.steps[i].description = step["description"]
            onboarding_process.steps[i].completed = step["completed"]
        return onboarding_process
