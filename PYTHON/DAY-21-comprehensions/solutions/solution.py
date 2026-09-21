# Reference solution — attempt first.
servers=[{'name':'web-01','state':'running'},{'name':'db-01','state':'stopped'}]
running=[x['name'] for x in servers if x['state']=='running']
print(running)
