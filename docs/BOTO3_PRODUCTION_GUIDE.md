# Boto3 Production Engineering Guide

## Sessions

Use explicit sessions when selecting profile or region. Do not create or store credentials in source code.

## Clients and resources

Prefer clients for predictable automation APIs. Use resources where their higher-level interface is genuinely useful.

## Pagination

Assume list APIs can return multiple pages. Use service paginators whenever available.

## Retries and timeouts

Bound SDK retries and network timeouts. Distinguish throttling/service failures from validation, authentication and authorization failures.

## Idempotency

Design reruns so the intended result is stable. Use AWS idempotency tokens where supported.

## Safety

Default to read-only. Destructive actions must require explicit confirmation and should report exactly what will change.

## Multi-account and multi-region

Treat account ID and region as first-class fields in every inventory record.

## Observability

Log operation, account, region, resource ID and outcome. Never log secrets or tokens.