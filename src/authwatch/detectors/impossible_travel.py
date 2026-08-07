"""
Impossible travel detection rule.
"""


def detect_impossible_travel(events):

    countries = set()

    for event in events:
        country = event.get("country")

        if country:
            countries.add(country)

    if len(countries) >= 2:
        return {
            "alert": "Impossible Travel Detected",
            "severity": "High",
            "countries": list(countries)
        }

    return None
