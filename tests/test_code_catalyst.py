from code_catalyst import CodeCatalyst, Feedback

def test_share_prototype():
    cc = CodeCatalyst()
    prototype_id = "123"
    prototype_url = "https://example.com/prototype"
    shared_url = cc.share_prototype(prototype_id, prototype_url)
    assert shared_url == f"{prototype_url}?prototype_id={prototype_id}"

def test_collect_feedback():
    cc = CodeCatalyst()
    prototype_id = "123"
    prototype_url = "https://example.com/prototype"
    cc.share_prototype(prototype_id, prototype_url)
    user_feedback = "This is great!"
    cc.collect_feedback(prototype_id, user_feedback)
    feedback = cc.view_feedback(prototype_id)
    assert len(feedback) == 1
    assert feedback[0].prototype_url == prototype_url
    assert feedback[0].user_feedback == user_feedback

def test_view_feedback():
    cc = CodeCatalyst()
    prototype_id = "123"
    prototype_url = "https://example.com/prototype"
    cc.share_prototype(prototype_id, prototype_url)
    user_feedback = "This is great!"
    cc.collect_feedback(prototype_id, user_feedback)
    feedback = cc.view_feedback(prototype_id)
    assert len(feedback) == 1
    assert feedback[0].prototype_url == prototype_url
    assert feedback[0].user_feedback == user_feedback

def test_analyze_feedback():
    cc = CodeCatalyst()
    prototype_id = "123"
    prototype_url = "https://example.com/prototype"
    cc.share_prototype(prototype_id, prototype_url)
    user_feedback1 = "This is great!"
    user_feedback2 = "This is great!"
    user_feedback3 = "This is bad!"
    cc.collect_feedback(prototype_id, user_feedback1)
    cc.collect_feedback(prototype_id, user_feedback2)
    cc.collect_feedback(prototype_id, user_feedback3)
    analysis = cc.analyze_feedback(prototype_id)
    assert analysis[user_feedback1] == 2
    assert analysis[user_feedback3] == 1
