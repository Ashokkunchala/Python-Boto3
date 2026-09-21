# Day 60 Exercises

## Objective
Practice final capstone.

## Main task
Deliver a tested read-only multi-account/multi-region inventory and compliance scanner.

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
