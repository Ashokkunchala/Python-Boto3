# Day 17 — Subprocess

## Goal
Run operating-system commands from Python carefully.

## Example
```python
import subprocess
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
```

## Exercises
Capture output; inspect return codes; avoid shell injection.

## Mini challenge
Create a command health checker.

## DevOps connection
Connect Python with Linux/Windows tooling.

## Checklist
- [ ] I understand the concept.
- [ ] I typed the example myself.
- [ ] I completed the exercises.
- [ ] I completed the mini challenge.
- [ ] I can explain where this helps in DevOps.
