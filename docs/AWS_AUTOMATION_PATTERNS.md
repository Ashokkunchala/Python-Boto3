# AWS Automation Patterns

## Read-only inventory
Collect resources without mutating state. Include account, region, resource ID, state and timestamp.

## Safe mutation
Require an explicit flag and a second confirmation for destructive actions. Print the exact resource set before execution.

## Pagination
Never assume the first response is complete.

## Retry
Retry throttling and transient service failures with bounded SDK behavior. Do not blindly retry validation or authorization errors.

## Idempotency
Use deterministic identifiers and AWS idempotency tokens where available.

## Partial failure
For multi-region or multi-account scans, record per-target failures and continue where policy permits. The final report must distinguish success, skipped and failed targets.

## Rate control
Bound worker concurrency. Prefer SDK adaptive retry behavior and avoid unbounded thread pools.

## Credential isolation
Use profiles, SSO or assumed roles. Never embed access keys in code or config committed to Git.

## Evidence
Every automation should make its result auditable: operation, account, region, resource, timestamp and outcome.