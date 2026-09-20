# Multi-Account Automation Design

A production scanner should not copy credentials for every account.

Preferred pattern:

1. Start with a trusted operator identity.
2. Discover target accounts from Organizations or a configured inventory.
3. Assume a dedicated read-only audit role in each target account.
4. Create a Boto3 session using the temporary credentials.
5. Scan enabled regions.
6. Emit account and region in every record.
7. Isolate failures per account/region.
8. Store the resulting evidence centrally.

## Security

Use the smallest trust relationship and permissions required by the scanner. Keep the audit role read-only.

## Reliability

One failed account must not discard results from every other account. Reports should contain success, skipped and failed targets separately.