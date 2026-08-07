"""
Detection analysis engine.
"""

from .detectors.brute_force import detect_brute_force
from .detectors.blocklist import detect_blocklisted_ip
from .detectors.new_country import detect_new_country
from .detectors.admin_login import detect_admin_login


def analyze_events(events):
    """
    Analyze authentication events and generate alerts.
    """

    alerts = []

    # Brute force detection
    brute_force_alert = detect_brute_force(events)

    if brute_force_alert:
        alerts.append(brute_force_alert)

    # Blocklisted IP detection
    blocklist = [
        "10.10.10.5"
    ]

    for event in events:
        alert = detect_blocklisted_ip(event, blocklist)

        if alert:
            alerts.append(alert)

    # New country detection
    known_countries = [
        "Malaysia"
    ]

    for event in events:
        alert = detect_new_country(event, known_countries)

        if alert:
            alerts.append(alert)

    # Administrator login detection
    for event in events:
        alert = detect_admin_login(event)

        if alert:
            alerts.append(alert)

    return alerts
