# Day 38 — EC2 with Boto3

## Goal
Describe, filter and report EC2 instances safely.

## Example
```python
response = ec2.describe_instances()
```

## Exercises
1. Read the official Boto3 API shape for today's service/topic.
2. Write a read-only script.
3. Add clear error handling.

## Mini challenge
Create a read-only AWS report for today's topic. Do not delete or modify resources.

## Safety rule
Start with read-only operations. Never place access keys in source code. Use the AWS credential chain/profile configuration.

## DevOps connection
This is where Python fundamentals become AWS automation.

## Checklist
- [ ] I understand the concept.
- [ ] I can explain the API call.
- [ ] I tested read-only behavior.
- [ ] I handled likely errors.
