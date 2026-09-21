# Reference solution — attempt the exercise first.
import argparse
p=argparse.ArgumentParser()
p.add_argument('--environment', required=True)
p.add_argument('--region', default='ap-south-1')
args=p.parse_args()
print(args.environment, args.region)

