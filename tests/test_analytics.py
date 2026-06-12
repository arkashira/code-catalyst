from src.analytics import Analytics, ABTesting, NotificationSystem
import pytest

def test_track_page_view():
    analytics = Analytics()
    analytics.track_page_view(1, "home")
    assert len(analytics.page_views) == 1

def test_calculate_user_engagement():
    analytics = Analytics()
    analytics.calculate_user_engagement(1, 0.5)
    assert analytics.user_engagement[1] == 0.5

def test_get_page_views():
    analytics = Analytics()
    analytics.track_page_view(1, "home")
    analytics.track_page_view(1, "about")
    analytics.track_page_view(2, "home")
    assert analytics.get_page_views() == {1: 2, 2: 1}

def test_get_user_engagement():
    analytics = Analytics()
    analytics.calculate_user_engagement(1, 0.5)
    analytics.calculate_user_engagement(2, 0.7)
    assert analytics.get_user_engagement() == {1: 0.5, 2: 0.7}

def test_create_experiment():
    ab_testing = ABTesting()
    ab_testing.create_experiment("experiment_1")
    assert "experiment_1" in ab_testing.experiments

def test_update_experiment():
    ab_testing = ABTesting()
    ab_testing.create_experiment("experiment_1")
    ab_testing.update_experiment("experiment_1", "variant_a")
    assert ab_testing.get_experiment_results("experiment_1") == {"variant_a": 1, "variant_b": 0}

def test_send_notification():
    notification_system = NotificationSystem()
    notification_system.send_notification("Notification 1")
    assert len(notification_system.get_notifications()) == 1
