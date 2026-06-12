from auth import generate_jwt_middleware, set_role_definitions, toggle_authentication
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

def test_generate_jwt_middleware():
    auth_config = AuthConfig(enabled=True, pages={})
    middleware = generate_jwt_middleware(auth_config)
    assert middleware.startswith("def jwt_middleware(request):")

def test_generate_jwt_middleware_disabled():
    auth_config = AuthConfig(enabled=False, pages={})
    middleware = generate_jwt_middleware(auth_config)
    assert middleware == ""

def test_set_role_definitions():
    auth_config = AuthConfig(enabled=True, pages={})
    roles = {"admin": Role("admin", {"read": True, "write": True})}
    auth_config = set_role_definitions("home", roles, auth_config)
    assert auth_config.pages["home"].roles == roles

def test_toggle_authentication():
    auth_config = AuthConfig(enabled=True, pages={})
    auth_config = toggle_authentication(auth_config, False)
    assert auth_config.enabled == False
