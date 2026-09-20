from __future__ import annotations

import argparse
import json

from aws_automation.boto import aws_session
from aws_automation.inventory import enabled_regions


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only enabled-region inventory")
    parser.add_argument("--profile")
    args = parser.parse_args()
    print(json.dumps(enabled_regions(aws_session(args.profile)), indent=2))


if __name__ == "__main__":
    main()
