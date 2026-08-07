"""
AuthWatch detection analyzer.
"""

from detectors.brute_force import detect_brute_force
from detectors.blocklist import detect_blocklisted_ip
from detectors.impossible_travel import detect_impossible_travel
from detectors.new_country import detect_new_country
from detectors.admin_login import detect_admin_login
from risk import calculate_risk_score


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

    # New country login detection
    new_country_alerts = detect_new_country(events)

    alerts.extend(new_country_alerts)

    # Administrator login detection
    admin_alerts = detect_admin_login(events)

    alerts.extend(admin_alerts)

    # Risk scoring
    risk_result = calculate_risk_score(alerts)

    return {
        "alerts": alerts,
        "risk": risk_result
    }
