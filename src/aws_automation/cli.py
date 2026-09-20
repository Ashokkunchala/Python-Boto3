from __future__ import annotations

import argparse
import json
import logging

from .boto import aws_session
from .inventory import ec2_instances, enabled_regions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AWS automation learning CLI")
    parser.add_argument("--profile")
    parser.add_argument("--region")
    parser.add_argument("--log-level", default="INFO")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("regions", help="List enabled AWS regions")
    ec2 = sub.add_parser("ec2", help="List EC2 instances")
    ec2.add_argument("--state", choices=["pending", "running", "stopping", "stopped", "shutting-down", "terminated"])
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level, format="%(asctime)s %(levelname)s %(message)s")
    session = aws_session(args.profile, args.region)
    if args.command == "regions":
        print(json.dumps(enabled_regions(session), indent=2))
        return
    client = session.client("ec2")
    rows = []
    for instance in ec2_instances(client):
        if args.state and instance.get("State", {}).get("Name") != args.state:
            continue
        rows.append({"id": instance.get("InstanceId"), "state": instance.get("State", {}).get("Name"), "type": instance.get("InstanceType"), "az": instance.get("Placement", {}).get("AvailabilityZone")})
    print(json.dumps(rows, indent=2, default=str))


if __name__ == "__main__":
    main()
