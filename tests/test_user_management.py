from user_management import UserManagement, Role

def test_invite_user():
    user_management = UserManagement()
    email = "test@example.com"
    role = Role.ADMIN
    assert user_management.invite_user(email, role) == f"Invitation sent to {email} with role {role.value}"

def test_get_user_role():
    user_management = UserManagement()
    email = "test@example.com"
    role = Role.ADMIN
    user_management.invite_user(email, role)
    assert user_management.get_user_role(email) == role.value

def test_send_invitation_email():
    user_management = UserManagement()
    email = "test@example.com"
    project_link = "https://example.com/project"
    assert user_management.send_invitation_email(email, project_link) == f"Email sent to {email} with link {project_link}"

def test_join_project():
    user_management = UserManagement()
    email = "test@example.com"
    project_link = "https://example.com/project"
    user_management.invite_user(email, Role.ADMIN)
    assert user_management.join_project(email, project_link) == f"{email} joined project {project_link}"
