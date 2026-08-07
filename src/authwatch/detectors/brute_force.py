"""
Brute force detection rule.
"""


def detect_brute_force(events, threshold=5):
    """
    Detect repeated failed login attempts.

    Args:
        events: authentication events list
        threshold: number of failures considered suspicious

    Returns:
        Detection alert if brute force is detected.
    """

    failed_attempts = 0

    for event in events:
        if event.get("status") == "failed":
            failed_attempts += 1

    if failed_attempts >= threshold:
        return {
            "alert": "Brute Force Attack Detected",
            "severity": "High",
            "failed_attempts": failed_attempts
        }

    return None
