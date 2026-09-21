# Read-only reference solution.
import boto3
client=boto3.client('ec2', region_name='ap-south-1')
waiter=client.get_waiter('instance_running')
print(waiter.name)
