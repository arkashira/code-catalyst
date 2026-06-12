from dataclasses import dataclass
from datetime import datetime

@dataclass
class TeamMember:
    name: str
    role: str
    changes: list

    def add_change(self, change):
        self.changes.append({"change": change, "timestamp": datetime.now().isoformat()})

    def revoke_access(self):
        self.role = "revoked"
