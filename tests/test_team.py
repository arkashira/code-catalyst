import pytest
from src.team import Team, TeamMember, Change

def test_team_init():
    team = Team()
    assert team.members == []
    assert team.changes == []

def test_add_member():
    team = Team()
    member = TeamMember("John Doe", "Developer")
    team.add_member(member)
    assert team.members == [member]

def test_add_change():
    team = Team()
    member = TeamMember("John Doe", "Developer")
    team.add_member(member)
    change = Change(member, "Fixed bug", "2022-01-01")
    team.add_change(change)
    assert team.changes == [change]

def test_revoke_access():
    team = Team()
    member1 = TeamMember("John Doe", "Developer")
    member2 = TeamMember("Jane Doe", "Manager")
    team.add_member(member1)
    team.add_member(member2)
    team.revoke_access(member1)
    assert team.members == [member2]
