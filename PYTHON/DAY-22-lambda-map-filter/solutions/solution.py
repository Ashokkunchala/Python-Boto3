# Reference solution — attempt first.
services=['ec2','s3','rds']
names=list(map(str.upper, services))
print(list(filter(lambda x: x.startswith('E'), names)))
