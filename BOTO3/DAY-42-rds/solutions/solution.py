# Read-only reference solution.
import boto3
client=boto3.client('rds', region_name='ap-south-1')
for db in client.describe_db_instances().get('DBInstances',[]): print(db['DBInstanceIdentifier'],db['DBInstanceStatus'])
