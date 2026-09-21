# Environment Setup

## Supported Python
Use Python 3.10+; Python 3.12 is used in CI. Python 3.13 is also suitable for the learning exercises.

## Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -e .
pytest
```

## Linux / WSL
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -e .
pytest
```

## Verify
```bash
python --version
pytest
ruff check .
```

Do not configure AWS credentials until the Boto3 phase. For AWS work, prefer named profiles or role-based credentials rather than access keys in source code.
