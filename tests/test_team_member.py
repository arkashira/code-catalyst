from src.team_member import TeamMember
import pytest

def test_team_member():
    team_member = TeamMember("John Doe", "Developer", [])
    assert team_member.name == "John Doe"
    assert team_member.role == "Developer"
    assert team_member.changes == []

def test_add_change():
    team_member = TeamMember("John Doe", "Developer", [])
    team_member.add_change("Added new feature")
    assert len(team_member.changes) == 1

def test_revoke_access():
    team_member = TeamMember("John Doe", "Developer", [])
    team_member.revoke_access()
    assert team_member.role == "revoked"
