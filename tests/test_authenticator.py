from src.authenticator import Authenticator
import pytest

def test_authenticator():
    authenticator = Authenticator()
    authenticator.register_user("user1", "password1")
    assert authenticator.authenticate("user1", "password1") == True
    assert authenticator.authenticate("user1", "wrong_password") == False
    assert authenticator.authenticate("non_existent_user", "password") == False
