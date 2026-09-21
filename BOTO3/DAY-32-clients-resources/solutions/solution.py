# Read-only reference solution.
import boto3
session=boto3.Session(region_name='ap-south-1')
ec2=session.client('ec2')
print(ec2.meta.service_model.service_name)
