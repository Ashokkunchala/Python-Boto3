# Read-only reference solution.
import boto3
client=boto3.client('cloudwatch', region_name='ap-south-1')
print(len(client.list_metrics().get('Metrics',[])))
