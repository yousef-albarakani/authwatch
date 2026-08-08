"""AuthWatch JSON reporting."""

import json
from pathlib import Path


def save_report(alerts, risk, output_file="reports/authwatch_report.json"):
    """Save AuthWatch alerts and risk assessment as a JSON report."""
    report = {
        "tool": "AuthWatch",
        "alerts": alerts,
        "risk_assessment": risk,
    }

    report_path = Path(output_file)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return str(report_path)
