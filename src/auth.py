import hashlib
from dataclasses import dataclass
from typing import Dict
from config import save_config

@dataclass
class User:
    id: str
    name: str
    email: str

class Auth:
    def __init__(self, config):
        self.config = config
        self.users = {}
        self.session_tokens = {}

    def enable_auth(self):
        self.config.auth_enabled = True
        save_config('config.json', self.config)

    def disable_auth(self):
        self.config.auth_enabled = False
        save_config('config.json', self.config)

    def login(self, provider: str, user_data: Dict):
        user_id = hashlib.sha256(user_data['email'].encode()).hexdigest()
        user = User(user_id, user_data['name'], user_data['email'])
        self.users[user_id] = user
        session_token = hashlib.sha256(user_id.encode()).hexdigest()
        self.session_tokens[session_token] = user_id
        return session_token

    def validate_session_token(self, session_token: str):
        if session_token in self.session_tokens:
            return self.users[self.session_tokens[session_token]]
        return None
