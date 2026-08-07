# AuthWatch

> Defensive Python tool for detecting suspicious Windows authentication activity.

## Overview

AuthWatch is a defensive cybersecurity tool designed to analyze authentication logs and identify suspicious login activity.

The project simulates a practical Blue Team / SOC workflow by transforming authentication events into security alerts that can be investigated by a security analyst.

---

## Detection Capabilities

AuthWatch detects suspicious authentication activities including:

- Brute-force login attempts
- Blocklisted IP addresses
- Impossible travel activity
- Logins from previously unseen countries
- Administrator account logins

---

## Security Workflow

```text
Authentication Logs
        |
        v
    Log Parser
        |
        v
 Detection Engine
        |
        v
 Security Rules
        |
        v
 Risk Assessment
        |
        v
 Alert Output
Project Goals
AuthWatch demonstrates practical Blue Team skills in:
Security log analysis
Threat detection
Python programming
Detection engineering
SOC analyst workflows
Security automation
Incident investigation
MITRE ATT&CK mapping
Example Detection Scenarios
Brute Force Detection
Detects repeated failed authentication attempts that may indicate password-guessing attacks.
Blocklisted IP Detection
Identifies authentication activity from known suspicious IP addresses.
Impossible Travel Detection
Detects suspicious login activity where location and time differences are unrealistic.
New Country Login Detection
Flags authentication from countries not previously associated with the user.
Administrator Login Detection
Highlights privileged account activity for additional security review.
Technology Stack
Python
JSONL Authentication Logs
Unit Testing
MITRE ATT&CK
Command-Line Interface
Project Structure
authwatch/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── authwatch/
│       ├── main.py
│       ├── parser.py
│       ├── analyzer.py
│       │
│       ├── detectors/
│       │   ├── brute_force.py
│       │   ├── blocklist.py
│       │   ├── impossible_travel.py
│       │   ├── new_country.py
│       │   └── admin_login.py
│       │
│       └── reporting.py
│
├── logs/
│   └── sample_authentication.jsonl
│
├── tests/
│
├── docs/
│
└── screenshots/
MITRE ATT&CK Mapping
Detection logic will be mapped to relevant MITRE ATT&CK techniques.
This demonstrates how security detections relate to real-world attacker behavior.
Testing
The project includes automated testing for detection logic and core functionality.
Tests ensure detection rules behave consistently as the project develops.
Defensive Purpose
AuthWatch is designed for:
Defensive security education
Security monitoring practice
SOC analyst training
Authorized laboratory environments
All sample authentication logs are synthetic and created for safe demonstrations.
Roadmap

Initial project concept

Authentication log parser

Brute-force detection

Blocklisted IP detection

Impossible-travel detection

New-country detection

Administrator-login detection

Risk scoring

MITRE ATT&CK mapping

Unit tests

Reporting improvements

Documentation

Screenshots

First release
Author
Yousef Haroon Al-Barakani
Cybersecurity Student
Asia Pacific University (APU)
