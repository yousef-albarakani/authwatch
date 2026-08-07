"""
AuthWatch risk scoring system.
"""


def calculate_risk_score(alerts):

    score = 0

    for alert in alerts:

        alert_type = alert.get("alert")

        if alert_type == "Brute Force Detected":
            score += 40

        elif alert_type == "Blocklisted IP Detected":
            score += 50

        elif alert_type == "Impossible Travel Detected":
            score += 35

        elif alert_type == "New Country Login Detected":
            score += 20

        elif alert_type == "Administrator Login Detected":
            score += 30

    if score >= 71:
        risk_level = "High"

    elif score >= 31:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    return {
        "risk_score": score,
        "risk_level": risk_level
    }
