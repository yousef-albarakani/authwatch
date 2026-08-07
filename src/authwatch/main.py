"""
AuthWatch main execution module.
"""
 
import json

from analyzer import analyze_events


def load_logs(file_path):

    events = []

    with open(file_path, "r") as file:

        for line in file:
            if line.strip():
                events.append(json.loads(line))

    return events


def main():

    log_file = "logs/sample_authentication.jsonl"

    events = load_logs(log_file)

    result = analyze_events(events)

    print("\n=== AuthWatch Security Report ===\n")

    print("Alerts:")

    for alert in result["alerts"]:
        print("-----------------------------")
        print(f"Alert: {alert.get('alert')}")
        print(f"Severity: {alert.get('severity')}")
        print(f"User: {alert.get('username')}")

    print("\nRisk Assessment:")
    print(f"Risk Score: {result['risk']['risk_score']}")
    print(f"Risk Level: {result['risk']['risk_level']}")


if __name__ == "__main__":
    main()
