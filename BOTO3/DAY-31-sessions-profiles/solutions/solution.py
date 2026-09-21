# Read-only reference solution.
import boto3
session=boto3.Session(profile_name=None, region_name='ap-south-1')
print(session.region_name)
