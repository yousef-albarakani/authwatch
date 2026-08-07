"""
Impossible travel detection rule.
"""


def detect_impossible_travel(previous_login, current_login):
    """
    Detect suspicious login activity where travel distance
    and login timing are unrealistic.
    
    Args:
        previous_login: previous authentication event
        current_login: current authentication event

    Returns:
        Detection alert if impossible travel is detected.
    """

    previous_country = previous_login.get("country")
    current_country = current_login.get("country")

    previous_time = previous_login.get("timestamp")
    current_time = current_login.get("timestamp")

    if (
        previous_country != current_country
        and previous_time == current_time
    ):
        return {
            "alert": "Impossible Travel Detected",
            "severity": "Medium",
            "from": previous_country,
            "to": current_country
        }

    return None
