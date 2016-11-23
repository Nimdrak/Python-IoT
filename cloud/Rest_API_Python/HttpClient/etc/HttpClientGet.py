'''
Created on Mar 23, 2016

@author: nimdrak
'''

import json
from piston_mini_client.failhandlers import APIError
import requests


username = 'karaf'
password = 'karaf'


resp = requests.get("http://localhost:8181/onos/v1/flows/of:00009cebe831287a/",auth=(username,password))
if resp.status_code != 200:
    raise APIError('GET /tasks/ {}'.format(resp.status_code))
    
print json.dumps(resp.json(), sort_keys=True, indent=2, separators=(',',':'))

#    print('{}{}'.format(todo_item['id'].todo_item['summary']))
