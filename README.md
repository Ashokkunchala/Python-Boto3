# Python + Boto3 — AWS Automation Engineering

A practical repository for learning Python and Boto3 by building safe, reusable AWS automation.

## Learning path

1. Python automation foundations
2. Boto3 sessions, clients and resources
3. Pagination, retries, waiters and error handling
4. EC2/VPC automation
5. S3 automation
6. IAM and security automation
7. RDS/DynamoDB/Lambda/SQS/CloudWatch
8. Multi-region and multi-account inventory
9. Testing and AWS mocking
10. Production CLI and capstone

## Engineering standard

**Discover → Validate → Plan → Apply → Verify → Report → Recover**

All examples are read-only by default. Destructive operations must require an explicit opt-in flag.

Never hard-code AWS credentials.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest
python -m aws_automation.cli --help
```

PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pip install -e .
pytest
python -m aws_automation.cli --help
```

## Structure

- `docs/` — learning and production patterns
- `src/aws_automation/` — reusable package
- `scripts/` — executable examples
- `tests/` — unit tests
- `examples/` — safe configuration examples
- `.github/workflows/` — CI