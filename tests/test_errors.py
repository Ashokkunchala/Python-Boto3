from botocore.exceptions import ClientError

from aws_automation.errors import format_client_error, is_retryable


def error(code: str) -> ClientError:
    return ClientError({"Error": {"Code": code, "Message": "test"}}, "DescribeSomething")


def test_throttling_is_retryable() -> None:
    assert is_retryable(error("ThrottlingException")) is True


def test_access_denied_is_not_retryable() -> None:
    assert is_retryable(error("AccessDenied")) is False


def test_error_format() -> None:
    assert format_client_error(error("AccessDenied")) == "AccessDenied: test"
