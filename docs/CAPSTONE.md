# Capstone — AWS Account Inventory + Compliance Scanner

## Objective

Build a read-only scanner that can inspect one or more AWS accounts and enabled regions and produce evidence reports.

## Required inventory

- Account identity
- Regions
- EC2 instances
- EBS volumes
- S3 buckets
- RDS instances
- IAM users/roles/policies
- Security groups

## Required engineering

- Boto3 Session per profile/account
- pagination
- bounded retries and timeouts
- structured logging
- per-account/per-region failure isolation
- JSON and CSV reports
- deterministic resource keys
- unit tests with mocks
- CI checks

## Compliance examples

- public security-group ingress
- unencrypted EBS volumes
- public S3 configuration
- RDS publicly accessible
- old or unused resources

The scanner must be read-only. Any remediation belongs in a separate explicitly-confirmed workflow.

## Final evidence

Architecture diagram, design notes, sample report, tests, failure drill and five-minute explanation.