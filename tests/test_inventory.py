from unittest.mock import Mock

from aws_automation.inventory import ec2_instances, enabled_regions


def test_ec2_instances_flattens_reservations() -> None:
    client = Mock()
    client.get_paginator.return_value.paginate.return_value = [{"Reservations": [{"Instances": [{"InstanceId": "i-1"}, {"InstanceId": "i-2"}]}]}]
    assert [item["InstanceId"] for item in ec2_instances(client)] == ["i-1", "i-2"]


def test_enabled_regions_sorts_names() -> None:
    session = Mock()
    session.client.return_value.describe_regions.return_value = {"Regions": [{"RegionName": "us-west-2"}, {"RegionName": "ap-south-1"}]}
    assert enabled_regions(session) == ["ap-south-1", "us-west-2"]
