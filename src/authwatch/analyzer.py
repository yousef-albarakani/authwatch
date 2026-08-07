"""
AuthWatch detection analyzer.
"""

from detectors.brute_force import detect_brute_force
from detectors.blocklist import detect_blocklisted_ip
from detectors.impossible_travel import detect_impossible_travel


def analyze_events(events):

    alerts = []

    # Brute force detection
    brute_force_alert = detect_brute_force(events)

    if brute_force_alert:
        alerts.append(brute_force_alert)

    # Blocklisted IP detection
    blocklist_alerts = detect_blocklisted_ip(events)

    alerts.extend(blocklist_alerts)

    # Impossible travel detection
    impossible_travel_alert = detect_impossible_travel(events)

    if impossible_travel_alert:
        alerts.append(impossible_travel_alert)

    return alerts
