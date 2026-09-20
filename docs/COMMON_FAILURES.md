# Common Boto3 Failure Drills

## AccessDenied
Capture the operation, account, region and requested resource. Confirm the caller identity, IAM policy and resource policy. Do not solve authorization errors by granting AdministratorAccess.

## Throttling
Check request rate and concurrency. Use bounded concurrency and SDK retry configuration. Separate transient throttling from quota exhaustion.

## Pagination
Compare resource counts with a console/API expectation. If the script stops after the first page, replace manual loops with a paginator.

## Partial regional failure
Continue scanning healthy regions while recording the failed region. Return a non-zero process status when required by the CI/job contract.

## Credentials
When a script suddenly loses access, verify profile/SSO/session state and STS caller identity before changing code.

## Duplicate inventory
Use a stable key such as account + region + service + resource ID. De-duplicate at aggregation time and investigate why the producer emitted duplicates.