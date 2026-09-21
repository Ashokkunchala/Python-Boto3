# Reference design — implement and test your own version first.
import csv
records=[{'service':'ec2','count':2}]
with open('report.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['service','count']); w.writeheader(); w.writerows(records)
