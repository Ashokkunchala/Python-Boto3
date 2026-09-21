# Read-only reference solution.
from botocore.exceptions import ClientError
try:
    raise ClientError({'Error':{'Code':'AccessDenied','Message':'example'}}, 'Example')
except ClientError as exc:
    print(exc.response['Error']['Code'])
