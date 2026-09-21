# Day 56 Exercises

## Objective
Practice tag compliance.

## Main task
Detect missing required tags without modifying resources.

## Production requirements
- Separate AWS collection from pure transformation logic.
- Use bounded retries and explicit timeouts.
- Handle pagination.
- Add structured logging.
- Preserve region/account context.
- Never hard-code credentials.

## Acceptance
The script must be understandable by another DevOps engineer and safe to run in read-only mode.

## Challenge
Add tests, JSON/CSV output, partial-failure handling and a useful CLI.
