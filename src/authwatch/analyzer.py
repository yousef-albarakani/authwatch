"""
Authentication log parser module.
"""

import json


def parse_logs(file_path):
    """
    Read authentication logs from JSONL file.
    """

    events = []

    with open(file_path, "r") as file:
        for line in file:
            event = json.loads(line)
            events.append(event)

    return events
