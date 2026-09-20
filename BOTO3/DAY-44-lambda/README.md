# Day 44 — Lambda with Boto3

## Goal
Inventory functions and configuration metadata.

## Example
```python
lambda_client.list_functions()
```

## Exercises
1. Build a read-only implementation.
2. Add pagination where the API supports it.
3. Add error handling and structured output.

## Mini challenge
Produce a useful operational report for today's topic.

## Safety rule
Keep learning scripts read-only unless the lesson explicitly introduces a controlled change with a rollback plan. Never hardcode credentials.

## DevOps connection
These patterns map directly to AWS inventory, troubleshooting, compliance and operational automation.

## Checklist
- [ ] Concept understood
- [ ] Read-only script works
- [ ] Errors are handled
- [ ] Output is useful
