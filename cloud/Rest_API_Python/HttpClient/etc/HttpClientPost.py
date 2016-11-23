'''
Created on Mar 23, 2016

@author: nimdrak
'''

import json
from piston_mini_client.failhandlers import APIError
import requests


username = 'karaf'
password = 'karaf'


task = {
      "deviceId":"of:00009cebe831287a",
      "isPermanent":"true",
      "priority":"65000",
      "state": "ADD",
      "treatment": {
                    "instructions": [
                                    ],
                    "deferred": []
                    },

      "selector": {
                   "criteria": [
                                    {
                                     "ethType": "0x0806",
                                     "type": "ETH_TYPE"
                                     }
                                ]
                   }
        
            
        }

data=json.dumps(task)

resp = requests.post("http://localhost:8181/onos/v1/flows/of:00009cebe831287a",data,auth=(username,password))

if resp.status_code != 201:
    raise APIError('POST /tasks/ {}'.format(resp.status_code))

