# Python + Boto3 Roadmap

This roadmap is now **beginner-first**. If you do not know Python, start at Day 1.

## Phase 1 — Python Foundations (Days 1–20)
Variables, data types, strings, lists, tuples, sets, dictionaries, conditions, loops, functions, modules, files, JSON/CSV, exceptions, debugging, pathlib, subprocess, argparse and logging.

## Phase 2 — Python Automation + Intermediate (Days 21–30)
Comprehensions, functional helpers, classes, OOP, dataclasses, generators, decorators/context managers, type hints, pytest and an automation mini-project.

## Phase 3 — Boto3 Fundamentals (Days 31–40)
Sessions, profiles, regions, clients, resources, paginators, waiters, ClientError, retries, timeouts and EC2/S3/IAM fundamentals.

## Phase 4 — AWS Services with Boto3 (Days 41–50)
VPC, RDS, DynamoDB, Lambda, SQS, CloudWatch, multi-region, multi-account and reporting.

## Phase 5 — AWS Automation Engineering (Days 51–60)
Account inventory, EC2/S3 inventory, normalized reporting, health checks, tag compliance, cost/operations data, safe changes, testing/CI and final capstone.

## Advanced track after Day 60
The existing `docs/` and `src/aws_automation/` content covers production engineering patterns: idempotency, dry-run, bounded retries, structured logs, least privilege, multi-account/multi-region automation and testing.

## Capstone
Build a read-only account inventory/compliance scanner that:
- identifies the current account
- scans selected regions
- inventories key AWS resources
- reports missing required tags
- produces JSON and CSV
- handles partial failures
- has unit tests
- has a safe CLI
