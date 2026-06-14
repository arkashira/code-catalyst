# User Management
A simple user management system for inviting team members to collaborate on a project.

## Features
* Invite team members via email
* Invited team members receive an email with a link to join the project
* Team members have appropriate access levels based on their roles

## Usage
1. Create a `UserManagement` instance
2. Invite a user with `invite_user(email, role)`
3. Send an invitation email with `send_invitation_email(email, project_link)`
4. Join a project with `join_project(email, project_link)`

## Testing
Run `python -m pytest` to execute the tests.
