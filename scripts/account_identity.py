from __future__ import annotations

import argparse
import json

from aws_automation.boto import aws_client


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only AWS account identity")
    parser.add_argument("--profile")
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    client = aws_client("sts", profile=args.profile, region=args.region)
    print(json.dumps(client.get_caller_identity(), indent=2, default=str))


if __name__ == "__main__":
    main()
