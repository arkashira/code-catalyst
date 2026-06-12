from user_management import UserManagement, Role

def test_invite_user():
    um = UserManagement()
    email = "test@example.com"
    role = Role.ADMIN
    result = um.invite_user(email, role)
    assert result == f"Invitation sent to {email} with role {role.value}"

def test_get_user_role():
    um = UserManagement()
    email = "test@example.com"
    role = Role.ADMIN
    um.invite_user(email, role)
    result = um.get_user_role(email)
    assert result == role

def test_send_invitation_email():
    um = UserManagement()
    email = "test@example.com"
    link = "https://example.com/join"
    um.send_invitation_email(email, link)
    # No assertion, just checking that the method runs without errors

def test_join_project():
    um = UserManagement()
    email = "test@example.com"
    role = Role.ADMIN
    um.invite_user(email, role)
    link = "https://example.com/join"
    um.join_project(email, link)
    # No assertion, just checking that the method runs without errors
