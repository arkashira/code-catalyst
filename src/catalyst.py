import json
import dataclasses
from datetime import datetime
from typing import List, Dict, Optional, Any

@dataclasses.dataclass
class Change:
    timestamp: str
    description: str

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class TeamMember:
    user_id: str
    name: str
    role: str
    changes: List[Change]
    active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "role": self.role,
            "active": self.active,
            "changes": [c.to_dict() for c in self.changes],
        }


class Dashboard:
    def __init__(self):
        self.members: Dict[str, TeamMember] = {}

    def add_member(self, user_id: str, name: str, role: str) -> None:
        if user_id not in self.members:
            self.members[user_id] = TeamMember(user_id, name, role, [])

    def record_change(self, user_id: str, description: str) -> bool:
        member = self.members.get(user_id)
        if not member or not member.active:
            return False
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        member.changes.append(Change(timestamp, description))
        return True

    def get_team_status(self) -> List[Dict[str, Any]]:
        return [m.to_dict() for m in self.members.values()]

    def revoke_access(self, user_id: str) -> bool:
        member = self.members.get(user_id)
        if member and member.active:
            member.active = False
            return True
        return False

    def to_json(self) -> str:
        return json.dumps([m.to_dict() for m in self.members.values()], indent=2)

    @classmethod
    def from_json(cls, data: str) -> 'Dashboard':
        obj = cls()
        data_list = json.loads(data)
        for item in data_list:
            member = TeamMember(
                user_id=item["user_id"],
                name=item["name"],
                role=item["role"],
                changes=[Change(**c) for c in item["changes"]],
                active=item["active"],
            )
            obj.members[member.user_id] = member
        return obj
