"""
AuthWatch reporting module.
"""

import json
import os


def save_report(alerts, risk, output_file="reports/authwatch_report.json"):
    """
    Save AuthWatch security results as a JSON report.
    """

    report = {
        "tool": "AuthWatch",
        "alerts": alerts,
        "risk_assessment": risk
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(report, file, indent=4)

    return output_file
