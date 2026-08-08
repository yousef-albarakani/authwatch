# AuthWatch

Defensive Python tool for analysing synthetic authentication logs and identifying suspicious login activity.

AuthWatch is a Blue Team / SOC portfolio project. It converts JSONL authentication events into detection alerts, a risk assessment, and a JSON report for investigation.

## Detection capabilities

- Brute-force login attempts
- Blocklisted IP addresses
- Impossible travel activity
- Logins from a new country
- Administrator account logins

## Project structure

```text
authwatch/
├── logs/
│   └── sample_authentication.jsonl
├── reports/
│   └── .gitkeep
├── src/
│   └── authwatch/
│       ├── detectors/
│       ├── analyzer.py
│       ├── main.py
│       ├── parser.py
│       ├── reporting.py
│       └── risk.py
├── tests/
│   ├── test_brute_force.py
│   └── test_detectors.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

`reports/authwatch_report.json` is generated when the application runs and is intentionally not committed.

## Run locally

From the repository root:

```powershell
python -m pip install --user -r requirements.txt
python -m pip install --user -e .
python -m authwatch.main
```

The report is written to `reports/authwatch_report.json`.

## Run unit tests

From the repository root:

```powershell
python -m pytest -q
```

## Defensive use

All authentication data in this repository is synthetic. AuthWatch is intended for defensive security education, SOC training, and authorised lab environments.

## Roadmap

- MITRE ATT&CK mapping
- Additional detection rules
- Richer reporting and documentation

## Author

Yousef Haroon Al-Barakani  
Cybersecurity Student, Asia Pacific University (APU)
