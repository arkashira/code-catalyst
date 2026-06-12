import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class Role(Enum):
    ADMIN = "admin"
    MEMBER = "member"

@dataclass
class User:
    email: str
    role: Role

class UserManagement:
    def __init__(self):
        self.users = {}

    def invite_user(self, email: str, role: Role):
        if email not in self.users:
            self.users[email] = User(email, role)
            return f"Invitation sent to {email} with role {role.value}"
        else:
            return f"User {email} already exists"

    def get_user_role(self, email: str):
        if email in self.users:
            return self.users[email].role
        else:
            return None

    def send_invitation_email(self, email: str, link: str):
        # Simulate sending an email
        print(f"Sending invitation email to {email} with link {link}")

    def join_project(self, email: str, link: str):
        if email in self.users:
            print(f"User {email} joined the project with link {link}")
        else:
            print(f"User {email} not found")
