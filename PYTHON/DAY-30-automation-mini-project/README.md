# Day 30 — Python Automation Mini Project

## Goal
Build a local system inventory CLI before touching AWS.

## Requirements
- Use argparse.
- Collect hostname and Python version.
- Read selected files/directories with pathlib.
- Capture one safe system command with subprocess.
- Write JSON and CSV.
- Use logging.
- Handle errors.
- Add pytest tests for pure functions.

## Suggested CLI
```text
python inventory.py --output reports/
```

## Acceptance criteria
- [ ] CLI has --help.
- [ ] JSON report is generated.
- [ ] CSV report is generated.
- [ ] Errors are logged clearly.
- [ ] No shell command is constructed from untrusted input.
- [ ] Tests pass locally.

This is the gate before starting Boto3.
