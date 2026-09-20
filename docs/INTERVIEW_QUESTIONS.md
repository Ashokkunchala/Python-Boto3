# Python + Boto3 Interview Bank

1. Session vs client vs resource?
2. How do paginators work?
3. How do you handle ClientError?
4. Why do retries require idempotency thinking?
5. How do you prevent credential leakage?
6. How would you scan every enabled region?
7. How would you scan multiple AWS accounts?
8. How do you prevent throttling at scale?
9. How do you test Boto3 code without real infrastructure?
10. How would you design a safe destructive CLI?

Scenario drills:
- EC2 inventory returns only some instances.
- An API starts throttling.
- S3 cleanup fails halfway through.
- IAM is denied in one account.
- One region becomes unavailable.
- A scheduled scanner executes twice.
- Inventory contains duplicates.

For each answer: state the failure mode, evidence, recovery and prevention.