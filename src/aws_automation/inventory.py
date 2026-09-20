from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def paginate(client: Any, operation: str, **kwargs: Any) -> Iterable[dict[str, Any]]:
    paginator = client.get_paginator(operation)
    yield from paginator.paginate(**kwargs)


def ec2_instances(client: Any) -> Iterable[dict[str, Any]]:
    for page in paginate(client, "describe_instances"):
        for reservation in page.get("Reservations", []):
            yield from reservation.get("Instances", [])


def enabled_regions(session: Any) -> list[str]:
    response = session.client("ec2", region_name="us-east-1").describe_regions(AllRegions=False)
    return sorted(item["RegionName"] for item in response.get("Regions", []))
