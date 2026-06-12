import pytest
from datetime import datetime
from catalyst import Dashboard, TeamMember, Change

def test_add_member():
    d = Dashboard()
    d.add_member("u1", "Alice", "Developer")
    status = d.get_team_status()
    assert len(status) == 1
    assert status[0]["user_id"] == "u1"
    assert status[0]["name"] == "Alice"
    assert status[0]["role"] == "Developer"
    assert status[0]["active"] is True
    assert status[0]["changes"] == []

def test_record_change():
    d = Dashboard()
    d.add_member("u1", "Alice", "Developer")
    success = d.record_change("u1", "Fixed login bug")
    assert success is True
    status = d.get_team_status()
    assert len(status[0]["changes"]) == 1
    change = status[0]["changes"][0]
    assert change["description"] == "Fixed login bug"
    # Check timestamp format
    dt = datetime.strptime(change["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    assert isinstance(dt, datetime)

def test_record_change_inactive_member():
    d = Dashboard()
    d.add_member("u1", "Alice", "Developer")
    d.revoke_access("u1")
    success = d.record_change("u1", "Tried to add change")
    assert success is False
    status = d.get_team_status()
    assert len(status[0]["changes"]) == 0

def test_revoke_access():
    d = Dashboard()
    d.add_member("u1", "Alice", "Developer")
    assert d.revoke_access("u1") is True
    status = d.get_team_status()
    assert status[0]["active"] is False
    assert d.revoke_access("u2") is False  # non-existent

def test_get_team_status_returns_all():
    d = Dashboard()
    d.add_member("u1", "Alice", "Founder")
    d.add_member("u2", "Bob", "Designer")
    d.record_change("u1", "Initial commit")
    d.record_change("u2", "Added UI mockup")
    d.revoke_access("u2")

    status = d.get_team_status()
    assert len(status) == 2
    found_u1 = next(m for m in status if m["user_id"] == "u1")
    found_u2 = next(m for m in status if m["user_id"] == "u2")

    assert found_u1["name"] == "Alice"
    assert found_u1["role"] == "Founder"
    assert len(found_u1["changes"]) == 1
    assert found_u1["changes"][0]["description"] == "Initial commit"

    assert found_u2["name"] == "Bob"
    assert found_u2["role"] == "Designer"
    assert found_u2["active"] is False
    assert len(found_u2["changes"]) == 1
    assert found_u2["changes"][0]["description"] == "Added UI mockup"

def test_serialization_roundtrip():
    d = Dashboard()
    d.add_member("u1", "Alice", "Dev")
    d.record_change("u1", "Code refactored")
    d.revoke_access("u1")

    json_data = d.to_json()
    d2 = Dashboard.from_json(json_data)

    assert d2.members["u1"].user_id == "u1"
    assert d2.members["u1"].name == "Alice"
    assert d2.members["u1"].role == "Dev"
    assert d2.members["u1"].active is False
    assert len(d2.members["u1"].changes) == 1
    assert d2.members["u1"].changes[0].description == "Code refactored"
