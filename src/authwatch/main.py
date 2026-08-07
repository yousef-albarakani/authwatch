"""
AuthWatch main entry point.
"""

from parser import parse_logs
from analyzer import analyze_events


def main():

    log_file = "logs/sample_authentication.jsonl"

    events = parse_logs(log_file)

    alerts = analyze_events(events)

    print("\n=== AuthWatch Security Alerts ===\n")

    for alert in alerts:
        print("Alert:", alert["alert"])
        print("Severity:", alert["severity"])
        print("-----------------------------")


if __name__ == "__main__":
    main()
