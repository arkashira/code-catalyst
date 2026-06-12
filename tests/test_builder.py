from src.builder import Builder, Role
import pytest

def test_enable_auth():
    builder = Builder()
    assert builder.enable_auth()

def test_generate_auth_middleware():
    builder = Builder()
    assert builder.generate_auth_middleware() == "auth_middleware"

def test_set_role_definition():
    builder = Builder()
    role = Role("admin", ["read", "write"])
    builder.set_role_definition("page1", role)
    assert builder.get_role_definition("page1").name == "admin"

def test_get_role_definition():
    builder = Builder()
    role = Role("admin", ["read", "write"])
    builder.set_role_definition("page1", role)
    assert builder.get_role_definition("page1").name == "admin"
