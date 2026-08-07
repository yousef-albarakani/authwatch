"""
AuthWatch detection analyzer.
"""

from detectors.brute_force import detect_brute_force
from detectors.blocklist import detect_blocklisted_ip


def analyze_events(events):

    alerts = []

    # Brute force detection
    brute_force_alert = detect_brute_force(events)

    if brute_force_alert:
        alerts.append(brute_force_alert)

    # Blocklisted IP detection
    blocklist_alerts = detect_blocklisted_ip(events)

    alerts.extend(blocklist_alerts)

    return alerts
