# Read-only reference solution.
import boto3
s3=boto3.client('s3', region_name='ap-south-1')
print([b['Name'] for b in s3.list_buckets().get('Buckets',[])])
