from tracker import Tracker, Metrics

def test_tracker_init():
    tracker = Tracker()
    assert tracker.metrics == Metrics()

def test_update_metrics():
    tracker = Tracker()
    tracker.update_metrics(visits=1, conversions=1, retention=1)
    assert tracker.metrics.visits == 1
    assert tracker.metrics.conversions == 1
    assert tracker.metrics.retention == 1

def test_get_metrics():
    tracker = Tracker()
    tracker.update_metrics(visits=1, conversions=1, retention=1)
    metrics = tracker.get_metrics()
    assert metrics.visits == 1
    assert metrics.conversions == 1
    assert metrics.retention == 1

def test_export_metrics():
    tracker = Tracker()
    tracker.update_metrics(visits=1, conversions=1, retention=1)
    metrics = tracker.export_metrics()
    assert metrics["visits"] == 1
    assert metrics["conversions"] == 1
    assert metrics["retention"] == 1

def test_track_user_action():
    tracker = Tracker()
    tracker.track_user_action("visit")
    assert tracker.metrics.visits == 1
    tracker.track_user_action("conversion")
    assert tracker.metrics.conversions == 1
    tracker.track_user_action("retention")
    assert tracker.metrics.retention == 1
