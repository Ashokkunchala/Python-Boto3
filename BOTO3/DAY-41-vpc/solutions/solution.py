# Read-only reference solution.
import boto3
client=boto3.client('ec2', region_name='ap-south-1')
for vpc in client.describe_vpcs().get('Vpcs',[]): print(vpc['VpcId'],vpc.get('CidrBlock'))
