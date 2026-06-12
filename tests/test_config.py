import pytest
from src.config import load_config, save_config, Config

def test_load_config():
    save_config('config.json', Config(True, {'google': 'https://google.com', 'github': 'https://github.com'}))
    config = load_config('config.json')
    assert config.auth_enabled
    assert config.oauth2_providers['google'] == 'https://google.com'
    assert config.oauth2_providers['github'] == 'https://github.com'

def test_save_config():
    config = Config(False, {'google': 'https://google.com', 'github': 'https://github.com'})
    save_config('config.json', config)
    loaded_config = load_config('config.json')
    assert not loaded_config.auth_enabled
    assert loaded_config.oauth2_providers['google'] == 'https://google.com'
    assert loaded_config.oauth2_providers['github'] == 'https://github.com'
