"""
Blocklisted IP detection rule.
"""


BLOCKLISTED_IPS = [
    "8.8.8.8",
    "192.168.1.50"
]


def detect_blocklisted_ip(events):

    alerts = []

    for event in events:
        if event.get("ip") in BLOCKLISTED_IPS:
            alerts.append({
                "alert": "Blocklisted IP Detected",
                "severity": "Medium",
                "ip": event.get("ip"),
                "username": event.get("username")
            })

    return alerts
