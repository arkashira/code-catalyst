import pytest
from prototype import Prototype, PrototypeManager, Feedback

def test_create_prototype():
    manager = PrototypeManager()
    id = "123"
    url = "https://example.com"
    manager.create_prototype(id, url)
    prototype = manager.get_prototype(id)
    assert prototype.id == id
    assert prototype.url == url

def test_share_prototype():
    manager = PrototypeManager()
    id = "123"
    url = "https://example.com"
    manager.create_prototype(id, url)
    shared_url = manager.share_prototype(id)
    assert shared_url == url

def test_collect_feedback():
    manager = PrototypeManager()
    id = "123"
    url = "https://example.com"
    manager.create_prototype(id, url)
    user_id = "user1"
    comment = "This is a great prototype!"
    manager.collect_feedback(id, user_id, comment)
    feedback = manager.view_feedback(id)
    assert len(feedback) == 1
    assert feedback[0].prototype_id == id
    assert feedback[0].user_id == user_id
    assert feedback[0].comment == comment

def test_view_feedback():
    manager = PrototypeManager()
    id = "123"
    url = "https://example.com"
    manager.create_prototype(id, url)
    user_id = "user1"
    comment = "This is a great prototype!"
    manager.collect_feedback(id, user_id, comment)
    feedback = manager.view_feedback(id)
    assert len(feedback) == 1
    assert feedback[0].prototype_id == id
    assert feedback[0].user_id == user_id
    assert feedback[0].comment == comment

def test_prototype_not_found():
    manager = PrototypeManager()
    id = "123"
    with pytest.raises(ValueError):
        manager.get_prototype(id)
    with pytest.raises(ValueError):
        manager.share_prototype(id)
    with pytest.raises(ValueError):
        manager.collect_feedback(id, "user1", "comment")
    with pytest.raises(ValueError):
        manager.view_feedback(id)
