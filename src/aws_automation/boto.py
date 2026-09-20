from __future__ import annotations

import boto3
from botocore.config import Config


def aws_session(profile: str | None = None, region: str | None = None) -> boto3.Session:
    """Create an explicit session without embedding credentials."""
    return boto3.Session(profile_name=profile, region_name=region)


def aws_client(service: str, *, profile: str | None = None, region: str | None = None):
    """Create a bounded client with SDK retry handling."""
    session = aws_session(profile, region)
    config = Config(
        retries={"mode": "adaptive", "max_attempts": 8},
        connect_timeout=5,
        read_timeout=60,
    )
    return session.client(service, config=config)
