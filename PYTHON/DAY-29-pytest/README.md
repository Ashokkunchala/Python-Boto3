# Day 29 — pytest

## Goal
Learn how to test Python functions before trusting automation.

## Example
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run:
```bash
pytest
```

## Exercises
1. Test a string formatter.
2. Test a function with valid input.
3. Test invalid input.
4. Add a test for an exception.

## Mini challenge
Write tests for a small inventory transformation function.

## DevOps connection
Tests prevent a small Python change from silently breaking AWS automation.

## Checklist
- [ ] I can write a test.
- [ ] I can run pytest.
- [ ] I tested normal and failure cases.
