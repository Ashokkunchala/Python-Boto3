from __future__ import annotations

import argparse
import json

from aws_automation.boto import aws_client
from aws_automation.inventory import ec2_instances


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only EC2 inventory")
    parser.add_argument("--profile")
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    client = aws_client("ec2", profile=args.profile, region=args.region)
    rows = [{"instance_id": i.get("InstanceId"), "state": i.get("State", {}).get("Name"), "type": i.get("InstanceType"), "az": i.get("Placement", {}).get("AvailabilityZone")} for i in ec2_instances(client)]
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
