# Read-only reference solution.
import boto3
sts=boto3.Session(region_name='ap-south-1').client('sts')
print(sts.get_caller_identity()['Account'])
