# Read-only reference solution.
import boto3
session=boto3.Session()
for region in ['ap-south-1','us-east-1']:
    print(region, len(session.client('ec2',region_name=region).describe_regions()['Regions']))
