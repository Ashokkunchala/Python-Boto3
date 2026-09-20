# Day 26 — Generators

## Goal
Process sequences lazily with yield.

## Example
```python
def names(items):
    for item in items:
        yield item["name"]
```

## Exercises
1. Recreate the example.
2. Modify it for DevOps-style data.
3. Explain why this technique is useful.

## Mini challenge
Build a small automation example using today's concept.

## DevOps connection
This is part of the foundation required before writing production Boto3 automation.

## Checklist
- [ ] Concept understood
- [ ] Example typed
- [ ] Exercises completed
- [ ] Challenge completed
