from unittest.mock import patch

from aws_automation.boto import aws_session, aws_client


def test_session_uses_profile_and_region() -> None:
    with patch("aws_automation.boto.boto3.Session") as session:
        aws_session("demo", "ap-south-1")
        session.assert_called_once_with(profile_name="demo", region_name="ap-south-1")


def test_client_builds_with_explicit_config() -> None:
    with patch("aws_automation.boto.boto3.Session") as session:
        aws_client("s3", profile="demo", region="ap-south-1")
        session.return_value.client.assert_called_once()
