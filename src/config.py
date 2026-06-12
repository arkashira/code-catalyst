import json
from dataclasses import dataclass

@dataclass
class Config:
    auth_enabled: bool
    oauth2_providers: dict

def load_config(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return Config(data['auth_enabled'], data['oauth2_providers'])

def save_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump({
            'auth_enabled': config.auth_enabled,
            'oauth2_providers': config.oauth2_providers
        }, f)
