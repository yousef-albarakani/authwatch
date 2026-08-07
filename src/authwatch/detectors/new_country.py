"""
New country login detection rule.
"""


def detect_new_country(events):

    alerts = []

    user_countries = {}

    for event in events:

        username = event.get("username")
        country = event.get("country")

        if not username or not country:
            continue

        # First country recorded for this user
        if username not in user_countries:
            user_countries[username] = country
            continue

        # Detect login from a new country
        if country != user_countries[username]:

            alerts.append({
                "alert": "New Country Login Detected",
                "severity": "Medium",
                "username": username,
                "country": country,
                "message": f"User logged in from a new country: {country}"
            })

            # Update known country
            user_countries[username] = country

    return alerts
