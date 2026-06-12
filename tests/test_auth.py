from src.auth import Auth, Role, User
import pytest

def test_add_role():
    auth = Auth()
    role = Role("admin", ["read", "write"])
    auth.add_role(role)
    assert role.name in auth.roles

def test_add_user():
    auth = Auth()
    role = Role("admin", ["read", "write"])
    auth.add_role(role)
    user = User("john", role)
    auth.add_user(user)
    assert user.username in auth.users

def test_generate_jwt():
    auth = Auth()
    role = Role("admin", ["read", "write"])
    auth.add_role(role)
    user = User("john", role)
    auth.add_user(user)
    jwt = auth.generate_jwt("john")
    assert jwt is not None

def test_authenticate():
    auth = Auth()
    role = Role("admin", ["read", "write"])
    auth.add_role(role)
    user = User("john", role)
    auth.add_user(user)
    jwt = auth.generate_jwt("john")
    assert auth.authenticate(jwt)
