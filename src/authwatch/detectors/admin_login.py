"""
Administrator login detection rule.

Detects authentication events involving privileged administrator accounts.
"""


def detect_admin_login(events):

    alerts = []

    admin_accounts = [
        "admin",
        "administrator",
        "root",
        "system",
        "superuser"
    ]

    for event in events:

        username = event.get("username")

        if not username:
            continue

        if username.lower() in admin_accounts:

            alerts.append({
                "alert": "Administrator Login Detected",
                "severity": "High",
                "username": username,
                "ip": event.get("ip"),
                "country": event.get("country"),
                "message": "Privileged administrator account login detected"
            })

    return alerts
