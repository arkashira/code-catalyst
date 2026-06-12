import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Role:
    """Simple role definition."""
    name: str
    permissions: List[str]

@dataclass
class User:
    """User linked to a Role."""
    username: str
    role: Role

class Auth:
    """Very small in‑memory auth manager."""
    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
        self.roles: Dict[str, Role] = {}

    # ---------------------------------------------------------------------
    # Role handling
    # ---------------------------------------------------------------------
    def add_role(self, role: Role) -> None:
        """Register a role by its name."""
        self.roles[role.name] = role

    # ---------------------------------------------------------------------
    # User handling
    # ---------------------------------------------------------------------
    def add_user(self, user: User) -> None:
        """Register a user."""
        self.users[user.username] = user

    # ---------------------------------------------------------------------
    # Token helpers (very naive JWT stand‑in)
    # ---------------------------------------------------------------------
    def generate_jwt(self, username: str) -> str | None:
        """Return a JSON string that mimics a JWT payload."""
        user = self.users.get(username)
        if user:
            return json.dumps({"username": username, "role": user.role.name})
        return None

    def authenticate(self, jwt: str) -> bool:
        """Validate the supplied JWT‑like string."""
        try:
            payload = json.loads(jwt)
            username = payload["username"]
            role_name = payload["role"]
            user = self.users.get(username)
            return bool(user and user.role.name == role_name)
        except (json.JSONDecodeError, KeyError):
            return False
