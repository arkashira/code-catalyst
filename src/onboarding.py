import time
from dataclasses import dataclass, field
from typing import List

@dataclass
class OnboardingStep:
    name: str
    duration: float  # seconds to simulate

@dataclass
class OnboardingManager:
    steps: List[OnboardingStep] = field(default_factory=lambda: [
        OnboardingStep("Create Account", 0.1),
        OnboardingStep("Verify Email", 0.1),
        OnboardingStep("Set Up Profile", 0.1),
    ])

    def complete_onboarding(self) -> float:
        """
        Simulate completing the onboarding process.
        Returns the total time taken in seconds.
        """
        start = time.time()
        for step in self.steps:
            time.sleep(step.duration)
        end = time.time()
        return end - start
