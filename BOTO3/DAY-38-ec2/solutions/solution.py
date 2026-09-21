# Read-only reference solution.
import boto3
client=boto3.client('ec2', region_name='ap-south-1')
response=client.describe_instances(MaxResults=5)
print(len(response.get('Reservations', [])))
