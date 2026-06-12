from auth import Auth, User

def test_enable_auth():
    auth = Auth()
    auth.enable_auth(True)
    assert auth.db['auth_enabled']

def test_authenticate_google():
    auth = Auth()
    user = auth.authenticate('google', 'token123')
    assert user
    assert user.username == 'john_doe'

def test_authenticate_github():
    auth = Auth()
    user = auth.authenticate('github', 'token456')
    assert user
    assert user.username == 'john_doe'

def test_validate_session():
    auth = Auth()
    user = auth.authenticate('google', 'token123')
    validated_user = auth.validate_session('token123')
    assert validated_user
    assert validated_user.username == 'john_doe'

def test_invalid_provider():
    auth = Auth()
    user = auth.authenticate('facebook', 'token789')
    assert user is None
