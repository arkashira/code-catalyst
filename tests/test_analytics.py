from analytics import Analytics, UserInteraction

def test_add_interaction():
    analytics = Analytics()
    interaction = UserInteraction(1, 0.5, 1)
    analytics.add_interaction(interaction)
    assert len(analytics.interactions) == 1

def test_get_metrics():
    analytics = Analytics()
    interaction1 = UserInteraction(1, 0.5, 1)
    interaction2 = UserInteraction(2, 0.7, 2)
    analytics.add_interaction(interaction1)
    analytics.add_interaction(interaction2)
    metrics = analytics.get_metrics()
    assert metrics["page_views"] == 3
    assert metrics["click_through_rate"] == 0.6
    assert metrics["user_sessions"] == 3

def test_export_data():
    analytics = Analytics()
    interaction1 = UserInteraction(1, 0.5, 1)
    interaction2 = UserInteraction(2, 0.7, 2)
    analytics.add_interaction(interaction1)
    analytics.add_interaction(interaction2)
    data = analytics.export_data()
    assert data == '[\n    {\n        "page_view": 1,\n        "click_through_rate": 0.5,\n        "user_session": 1\n    },\n    {\n        "page_view": 2,\n        "click_through_rate": 0.7,\n        "user_session": 2\n    }\n]'

def test_display_dashboard(capsys):
    analytics = Analytics()
    interaction1 = UserInteraction(1, 0.5, 1)
    interaction2 = UserInteraction(2, 0.7, 2)
    analytics.add_interaction(interaction1)
    analytics.add_interaction(interaction2)
    analytics.display_dashboard()
    captured = capsys.readouterr()
    assert "Dashboard:" in captured.out
    assert "Page Views: 3" in captured.out
    assert "Click Through Rate: 0.60" in captured.out
    assert "User Sessions: 3" in captured.out
