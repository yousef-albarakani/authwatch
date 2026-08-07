"""
New country login detection rule.
"""


def detect_new_country(events):

    known_country = None

    alerts = []

    for event in events:

        country = event.get("country")

        if known_country is None:
            known_country = country
            continue

        if country != known_country:
            alerts.append({
                "alert": "New Country Login Detected",
                "severity": "Medium",
                "country": country,
                "username": event.get("username")
            })

    return alerts
