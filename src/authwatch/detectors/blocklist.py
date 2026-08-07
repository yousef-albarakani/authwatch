"""
Blocklisted IP detection rule.
"""


def detect_blocklisted_ip(event, blocklist):
    """
    Detect authentication attempts from known malicious IP addresses.

    Args:
        event: authentication event
        blocklist: list of blocked IP addresses

    Returns:
        Detection alert if IP is blocklisted.
    """

    ip_address = event.get("ip")

    if ip_address in blocklist:
        return {
            "alert": "Blocklisted IP Address Detected",
            "severity": "High",
            "ip": ip_address
        }

    return None
