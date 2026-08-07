"""
AuthWatch detection analyzer.
"""

from detectors.brute_force import detect_brute_force


def analyze_events(events):

    alerts = []

    brute_force_alert = detect_brute_force(events)

    if brute_force_alert:
        alerts.append(brute_force_alert)

    return alerts
