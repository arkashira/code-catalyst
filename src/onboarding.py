import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional

@dataclass
class Step:
    title: str
    description: str
    completed: bool = False

@dataclass
class Onboarding:
    steps: List[Step]
    current_step: int = 0

    def add_step(self, title: str, description: str) -> None:
        self.steps.append(Step(title, description))

    def next_step(self) -> Optional[Step]:
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.current_step += 1
            return step
        return None

    def skip_step(self) -> Optional[Step]:
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            step.completed = True
            self.current_step += 1
            return step
        return None

    def mark_completed(self) -> None:
        if self.current_step > 0:
            self.steps[self.current_step - 1].completed = True

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Onboarding':
        steps = [Step(**step) for step in data['steps']]
        return cls(steps, data['current_step'])

    def save(self, filepath: str) -> None:
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, filepath: str) -> 'Onboarding':
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)
