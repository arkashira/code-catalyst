from config import load_config, save_config
from auth import Auth

def main():
    config = load_config('config.json')
    auth = Auth(config)
    if auth.config.auth_enabled:
        print("Auth is enabled")
    else:
        print("Auth is disabled")
    # Enable auth
    auth.enable_auth()
    config = load_config('config.json')
    if config.auth_enabled:
        print("Auth is enabled")
    # Login with Google
    user_data = {'name': 'John Doe', 'email': 'john@example.com'}
    session_token = auth.login('google', user_data)
    print(f"Session token: {session_token}")
    # Validate session token
    user = auth.validate_session_token(session_token)
    if user:
        print(f"User: {user.name} ({user.email})")
    else:
        print("Invalid session token")

if __name__ == "__main__":
    main()
