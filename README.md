# Python + Boto3 — Beginner → AWS Automation Engineer

**Starting from zero Python? This repository is designed for you.**

You do **not** need Python knowledge before starting. Do not jump into the existing production Boto3 package. Follow the learning path in order.

## 60-Day Roadmap

| Phase | Days | Focus |
|---|---:|---|
| 1 | 1–20 | Python foundations |
| 2 | 21–30 | Python automation + intermediate fundamentals |
| 3 | 31–40 | Boto3 fundamentals |
| 4 | 41–50 | AWS services with Boto3 |
| 5 | 51–60 | AWS automation engineering |

Start: [START_HERE.md](START_HERE.md)

## Daily learning method

1. Read the lesson.
2. Type every example yourself.
3. Run it locally.
4. Complete the exercises without copying.
5. Complete the mini challenge.
6. Explain the DevOps connection in your own words.
7. Mark progress only after you can reproduce the result.

## Repository structure

- `PYTHON/` — zero-to-intermediate Python lessons, Days 1–30
- `BOTO3/` — Boto3 fundamentals and AWS service lessons, Days 31–50
- `AWS_AUTOMATION/` — AWS automation projects and production patterns, Days 51–60
- `PROJECTS/` — practical project briefs
- `docs/` — advanced Boto3 and production engineering material
- `src/aws_automation/` — reusable production-oriented package
- `scripts/` — executable examples
- `tests/` — automated tests
- `examples/` — safe configuration examples

## Important

The existing `src/aws_automation/` and `docs/` material is intentionally retained as a **later-stage reference**. You do not need to understand it on Day 1.

### Safety

- Never hard-code AWS access keys or secrets.
- Prefer read-only AWS operations while learning.
- Use explicit profiles/roles and regions.
- Use dry-run and confirmation boundaries before mutations.
- Do not run destructive examples against production accounts.
- Clean up paid AWS resources after labs.

## Quick start — Day 1

You only need Python installed.

```bash
python --version
python PYTHON/DAY-01-hello-python/hello.py
```

If `hello.py` does not exist yet, create it from the Day 1 example and run it.

### PowerShell

```powershell
py --version
py your_file.py
```

## After Day 30

Only then install/configure AWS credentials and begin Boto3.

## Engineering standard

For the advanced track:

**Discover → Validate → Plan → Apply → Verify → Report → Recover**

All learning examples are read-only by default. Any mutating automation must require explicit opt-in, validation and a documented rollback strategy.

## Progress

Use [PROGRESS.md](PROGRESS.md) to track completion.

Additional references:
- [Python Cheat Sheet](PYTHON_CHEATSHEET.md)
- [Python Interview Questions](PYTHON_INTERVIEW.md)
- [Debugging Guide](DEBUGGING_GUIDE.md)
- [30-Day Plan](docs/30_DAY_PLAN.md)
- [Boto3 Production Guide](docs/BOTO3_PRODUCTION_GUIDE.md)
- [Testing Guide](docs/TESTING_GUIDE.md)
