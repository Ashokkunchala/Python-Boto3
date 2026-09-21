# Contributing

## Learning changes
Keep beginner lessons simple and runnable. Every day should have:
- explanation
- example
- exercises
- solution
- mini challenge
- DevOps connection
- completion checklist

## Code quality
- Python 3.10+ compatible unless a lesson explicitly teaches a newer feature.
- Prefer standard library for beginner exercises.
- Use type hints in production-track code.
- Add tests for reusable logic.
- Never commit credentials, tokens, private keys or real customer data.

## AWS safety
Read-only by default. Any mutation must document:
- required permissions
- validation
- dry-run behavior
- rollback
- cleanup

## Commit style
Use small, descriptive commits such as:
`Add Day 12 file handling exercises`
