'''
Created on Mar 24, 2016

@author: nimdrak
'''

import json
from piston_mini_client.failhandlers import APIError
import requests


username = 'karaf'
password = 'karaf'



resp = requests.delete("http://localhost:8181/onos/v1/flows/of:00009cebe831287a/20829148730339100/",auth=(username,password))
if resp.status_code != 200:
    raise APIError('DEL_FLOW /tasks/ {}'.format(resp.status_code))


