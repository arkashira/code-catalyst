import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    username: str
    email: str

class Auth:
    def __init__(self, db_file: str = 'auth.db'):
        self.db_file = db_file
        self.load_db()

    def load_db(self):
        try:
            with open(self.db_file, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}

    def save_db(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f)

    def enable_auth(self, enabled: bool):
        self.db['auth_enabled'] = enabled
        self.save_db()

    def authenticate(self, provider: str, token: str) -> Optional[User]:
        if provider not in ['google', 'github']:
            return None
        # Simulate authentication with a dummy user
        user = User(1, 'john_doe', 'john@example.com')
        self.db['session_tokens'] = self.db.get('session_tokens', {})
        self.db['session_tokens'][token] = user.__dict__
        self.save_db()
        return user

    def validate_session(self, token: str) -> Optional[User]:
        if 'session_tokens' not in self.db:
            return None
        user_data = self.db['session_tokens'].get(token)
        if user_data:
            return User(**user_data)
        return None
