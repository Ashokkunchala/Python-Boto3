# Day 54 — Resource Reporting

## Goal
Normalize resource records and export JSON/CSV reports.

## Example
```python
report = {"account": account_id, "resources": resources}
```

## Build requirements
- Separate discovery, validation, collection, transformation and reporting.
- Use explicit timeouts and bounded retries.
- Handle pagination.
- Use structured logging.
- Keep secrets out of source control.
- Add tests for pure logic and mock AWS boundaries.

## Mini challenge
Extend the example into a small operational tool with a clear CLI, JSON/CSV output and failure handling.

## Safety
Default to read-only and dry-run. Any mutating capability must require explicit input, have validation, be idempotent where possible, and document rollback.

## Checklist
- [ ] Code is understandable.
- [ ] Errors are handled.
- [ ] Tests exist.
- [ ] Output is useful.
- [ ] No credentials are hardcoded.
