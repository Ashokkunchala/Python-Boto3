# Reference solution — attempt the exercise first.
import json
servers=[{'name':'web-01','state':'running'},{'name':'db-01','state':'available'}]
print(json.dumps(servers, indent=2))

