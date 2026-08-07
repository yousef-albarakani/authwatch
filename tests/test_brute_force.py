"""
AuthWatch brute force detection tests.
"""

from src.authwatch.detectors.brute_force import detect_brute_force


def test_brute_force_detection():

    events = [
        {"status": "failed"},
        {"status": "failed"},
        {"status": "failed"},
        {"status": "failed"},
        {"status": "failed"}
    ]

    result = detect_brute_force(events)

    assert result is not None
    assert result["alert"] == "Brute Force Attack Detected"
