"""Unit tests for AuthWatch detection rules."""

from authwatch.detectors.admin_login import detect_admin_login
from authwatch.detectors.blocklist import detect_blocklisted_ip
from authwatch.detectors.brute_force import detect_brute_force
from authwatch.detectors.impossible_travel import detect_impossible_travel
from authwatch.detectors.new_country import detect_new_country


def test_brute_force_alert_at_threshold():
    events = [{"status": "failed"} for _ in range(5)]

    alert = detect_brute_force(events)

    assert alert["alert"] == "Brute Force Attack Detected"
    assert alert["severity"] == "High"
    assert alert["failed_attempts"] == 5


def test_brute_force_does_not_alert_below_threshold():
    events = [{"status": "failed"} for _ in range(4)]

    assert detect_brute_force(events) is None


def test_blocklist_returns_only_matching_events():
    events = [
        {"ip": "8.8.8.8", "username": "eve"},
        {"ip": "203.0.113.10", "username": "alice"},
    ]

    alerts = detect_blocklisted_ip(events)

    assert len(alerts) == 1
    assert alerts[0]["ip"] == "8.8.8.8"
    assert alerts[0]["username"] == "eve"


def test_impossible_travel_requires_two_countries():
    events = [{"country": "Malaysia"}, {"country": "United States"}]

    alert = detect_impossible_travel(events)

    assert alert["alert"] == "Impossible Travel Detected"
    assert set(alert["countries"]) == {"Malaysia", "United States"}


def test_new_country_login_alerts_when_user_location_changes():
    events = [
        {"username": "alice", "country": "Malaysia"},
        {"username": "alice", "country": "Singapore"},
    ]

    alerts = detect_new_country(events)

    assert len(alerts) == 1
    assert alerts[0]["username"] == "alice"
    assert alerts[0]["country"] == "Singapore"


def test_admin_login_is_case_insensitive():
    events = [{"username": "Administrator", "ip": "192.0.2.10", "country": "Malaysia"}]

    alerts = detect_admin_login(events)

    assert len(alerts) == 1
    assert alerts[0]["alert"] == "Administrator Login Detected"
    assert alerts[0]["username"] == "Administrator"
