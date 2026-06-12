from dataclasses import dataclass
from typing import List

@dataclass
class TeamMember:
    name: str
    role: str

@dataclass
class Change:
    team_member: TeamMember
    change: str
    timestamp: str

class Team:
    def __init__(self):
        self.members = []
        self.changes = []

    def add_member(self, member: TeamMember):
        self.members.append(member)

    def add_change(self, change: Change):
        self.changes.append(change)

    def revoke_access(self, member: TeamMember):
        self.members = [m for m in self.members if m != member]
