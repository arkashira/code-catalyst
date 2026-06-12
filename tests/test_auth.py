import pytest
from src.auth import Auth
from src.config import Config, load_config, save_config

def test_enable_auth():
    config = Config(False, {'google': 'https://google.com', 'github': 'https://github.com'})
    save_config('config.json', config)
    auth = Auth(load_config('config.json'))
    auth.enable_auth()
    config = load_config('config.json')
    assert config.auth_enabled

def test_disable_auth():
    config = Config(True, {'google': 'https://google.com', 'github': 'https://github.com'})
    save_config('config.json', config)
    auth = Auth(load_config('config.json'))
    auth.disable_auth()
    config = load_config('config.json')
    assert not config.auth_enabled

def test_login():
    config = Config(True, {'google': 'https://google.com', 'github': 'https://github.com'})
    save_config('config.json', config)
    auth = Auth(load_config('config.json'))
    user_data = {'name': 'John Doe', 'email': 'john@example.com'}
    session_token = auth.login('google', user_data)
    assert session_token

def test_validate_session_token():
    config = Config(True, {'google': 'https://google.com', 'github': 'https://github.com'})
    save_config('config.json', config)
    auth = Auth(load_config('config.json'))
    user_data = {'name': 'John Doe', 'email': 'john@example.com'}
    session_token = auth.login('google', user_data)
    user = auth.validate_session_token(session_token)
    assert user
    assert user.name == 'John Doe'
    assert user.email == 'john@example.com'
