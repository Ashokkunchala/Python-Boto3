# Day 47 Exercises

## Objective
Practice multi-region.

## Main task
Run the same read-only inventory across selected regions.

## Requirements
- Read-only by default.
- Use pagination when supported.
- Handle ClientError.
- Keep account/region context in every record.
- Export structured output where appropriate.

## Challenge
Add a second region/account without duplicating business logic.

## Safety
Do not use production accounts for experiments. Never store credentials in the repository.
