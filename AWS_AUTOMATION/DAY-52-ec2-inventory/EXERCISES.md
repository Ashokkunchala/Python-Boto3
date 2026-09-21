# Day 52 Exercises

## Objective
Practice EC2 inventory.

## Main task
Build normalized EC2 records across regions.

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
