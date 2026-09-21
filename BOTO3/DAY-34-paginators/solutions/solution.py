# Read-only reference solution.
import boto3
client=boto3.client('ec2', region_name='ap-south-1')
paginator=client.get_paginator('describe_instances')
for page in paginator.paginate():
    print(len(page.get('Reservations', [])))
