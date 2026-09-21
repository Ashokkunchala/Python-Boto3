# Day 48 Exercises

## Objective
Practice multi-account.

## Main task
Design profile/role-based account scanning without hardcoded credentials.

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
