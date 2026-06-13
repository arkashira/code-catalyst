from typing import Dict

class Authenticator:
    def __init__(self):
        self.users = {}

    def register_user(self, username: str, password: str):
        self.users[username] = password

    def authenticate(self, username: str, password: str) -> bool:
        return self.users.get(username) == password
