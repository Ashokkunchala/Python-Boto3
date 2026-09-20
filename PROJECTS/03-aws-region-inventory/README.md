# Project 3 — AWS Region Inventory

Build a read-only Boto3 script that:
- Gets the current caller identity.
- Lists enabled/available regions for a selected service.
- Accepts `--profile` and `--region`.
- Handles credential and ClientError failures.
- Outputs JSON.

Never hard-code credentials.
