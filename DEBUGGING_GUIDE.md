# Python Debugging Guide

1. Read the complete traceback.
2. Identify the file and line number.
3. Reproduce the smallest failing case.
4. Inspect the relevant values.
5. Check types with `type(value)`.
6. Add a breakpoint when needed.
7. Fix the cause, not only the symptom.
8. Re-run the smallest test.
9. Run the full test suite before committing.

## Common errors
- `NameError`: name is unavailable.
- `TypeError`: incompatible type operation.
- `ValueError`: invalid value.
- `KeyError`: dictionary key does not exist.
- `IndexError`: sequence index is out of range.
- `FileNotFoundError`: requested path does not exist.
