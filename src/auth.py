import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Role:
    name: str
    permissions: Dict[str, bool]

@dataclass
class Page:
    name: str
    roles: Dict[str, Role]

@dataclass
class AuthConfig:
    enabled: bool
    pages: Dict[str, Page]

def generate_jwt_middleware(auth_config: AuthConfig) -> str:
    if not auth_config.enabled:
        return ""
    middleware = "def jwt_middleware(request):\n"
    middleware += "    if not request.headers.get('Authorization'):\n"
    middleware += "        return 'Unauthorized', 401\n"
    middleware += "    token = request.headers['Authorization'].split()[1]\n"
    middleware += "    if token != 'valid_token':\n"
    middleware += "        return 'Forbidden', 403\n"
    return middleware

def set_role_definitions(page_name: str, roles: Dict[str, Role], auth_config: AuthConfig) -> AuthConfig:
    if page_name not in auth_config.pages:
        auth_config.pages[page_name] = Page(name=page_name, roles={})
    auth_config.pages[page_name].roles = roles
    return auth_config

def toggle_authentication(auth_config: AuthConfig, enabled: bool) -> AuthConfig:
    auth_config.enabled = enabled
    return auth_config
