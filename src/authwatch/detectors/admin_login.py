"""
Administrator login detection rule.
"""


def detect_admin_login(event):
    """
    Detect authentication events involving administrator accounts.

    Args:
        event: authentication event

    Returns:
        Detection alert if administrator login is detected.
    """

    username = event.get("username")
    role = event.get("role")

    if role == "admin":
        return {
            "alert": "Administrator Login Detected",
            "severity": "Medium",
            "username": username
        }

    return None
