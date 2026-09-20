# Testing Boto3 Automation

## Unit tests

Mock the Boto3 client at the module boundary. Test:

- successful API responses
- multiple pagination pages
- ClientError classification
- empty results
- partial failures
- malformed input

## Integration tests

Use a sandbox AWS account only when an integration test adds meaningful confidence.

Keep tests deterministic and clean up every resource.

## Contract rule

Never make the unit test suite depend on the developer's local AWS credentials.