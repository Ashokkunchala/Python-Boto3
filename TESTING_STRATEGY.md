# Testing Strategy

## Learning stage
Days 1–20 focus on manually running programs and understanding behavior.

## Intermediate stage
Days 21–30 introduce reusable functions and pytest.

## Boto3 stage
Do not require live AWS for unit tests. Separate:
1. AWS collection boundary
2. pure transformation logic
3. reporting
4. CLI parsing

Mock or stub the AWS boundary. Test transformation/reporting logic with deterministic data.

## Production stage
Every production automation change should have:
- unit tests
- failure-path tests
- input validation tests
- formatting/report tests
- CI lint/test checks

Live AWS integration tests should use an explicitly designated test account and never run automatically against production.
