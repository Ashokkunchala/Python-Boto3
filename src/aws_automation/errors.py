from botocore.exceptions import ClientError


def is_retryable(error: ClientError) -> bool:
    code = error.response.get("Error", {}).get("Code", "")
    return code in {"Throttling", "ThrottlingException", "RequestLimitExceeded", "TooManyRequestsException", "ServiceUnavailable", "InternalError", "InternalFailure"}


def format_client_error(error: ClientError) -> str:
    details = error.response.get("Error", {})
    return f"{details.get('Code', 'Unknown')}: {details.get('Message', str(error))}"
