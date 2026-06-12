import json
from dataclasses import dataclass

@dataclass
class TourStep:
    description: str
    next_button: str

class CodeCatalyst:
    def __init__(self):
        self.tour_steps = [
            TourStep("Welcome to Code Catalyst! This is the main dashboard.", "Next"),
            TourStep("Here you can view your projects and navigate to different sections.", "Next"),
            TourStep("This is the settings menu where you can replay the tour or skip it.", "Finish")
        ]
        self.current_step = 0
        self.settings = {"tour_skipped": False}

    def start_tour(self):
        if self.settings["tour_skipped"]:
            return "Tour skipped"
        return self.get_current_step()

    def get_current_step(self):
        if self.current_step < len(self.tour_steps):
            return self.tour_steps[self.current_step]
        return "Tour finished"

    def next_step(self):
        if self.current_step < len(self.tour_steps) - 1:
            self.current_step += 1
            return self.get_current_step()
        return "Tour finished"

    def skip_tour(self):
        self.settings["tour_skipped"] = True
        return "Tour skipped"

    def replay_tour(self):
        self.settings["tour_skipped"] = False
        self.current_step = 0
        return self.get_current_step()
