'''
Created on Mar 30, 2016

@author: nimdrak
'''


import requests
import json
from piston_mini_client.failhandlers import APIError


def Routing_rule_post(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))
    
def Routing_rule_post_just_ip(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP,Src_PORT,Dst_PORT, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))
    
def Routing_rule_post_udp(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP,Src_PORT,Dst_PORT, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                         "type":"UDP_SRC",
                                         "udpPort": Src_PORT
                                         },
                                         {
                                         "type":"UDP_DST",
                                         "udpPort": Dst_PORT
                                         },
                                         {
                                         "type":"IP_PROTO",
                                         "protocol": "17"
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))

def Routing_rule_post_tcp(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP,Src_PORT,Dst_PORT, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                         "type":"TCP_SRC",
                                         "tcpPort": Src_PORT
                                         },
                                         {
                                         "type":"TCP_DST",
                                         "tcpPort": Dst_PORT
                                         },
                                         {
                                         "type":"IP_PROTO",
                                         "protocol": "6"
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))



def Routing_rule_post_udp_only_dst_port(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP,Src_PORT,Dst_PORT, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                         "type":"UDP_DST",
                                         "udpPort": Dst_PORT
                                         },
                                         {
                                         "type":"IP_PROTO",
                                         "protocol": "17"
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))

def Routing_rule_post_tcp_only_dst_port(Device_id, Priority, Type, Out_port, Src_IP, Dst_IP,Src_PORT,Dst_PORT, ARP_IP, ARP_IP_Type):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
          "state": "ADD",
          "treatment": {
                        "instructions": [
                                         {
                                         "type": Type,
                                         "port": Out_port
                                         }
                                        ],
                        "deferred": []
                        },
    
          "selector": {
                       "criteria": [
                                         {
                                         "type":"IPV4_SRC",
                                         "ip": Src_IP
                                         },
                                         {
                                         "type":"IPV4_DST",
                                         "ip": Dst_IP
                                         },
                                         {
                                         "type":"TCP_DST",
                                         "tcpPort": Dst_PORT
                                         },
                                         {
                                         "type":"IP_PROTO",
                                         "protocol": "6"
                                         },
                                         {
                                          "ethType": ARP_IP,
                                          "type": ARP_IP_Type
                                         }
                                             
                                   ]
                       }
            
                
            }
    
    data=json.dumps(task)
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))


def Routing_rule_post_arp_drop(Device_id, Priority):
    

    username = 'karaf'
    password = 'karaf'

    
    task = {
            
          "deviceId": Device_id,
          "isPermanent":"true",
          "priority": Priority,
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
    
    resp = requests.post("http://localhost:8181/onos/v1/flows/" + Device_id + "/",data,auth=(username,password))

    
    if resp.status_code != 201:
        raise APIError('POST /tasks/ {}'.format(resp.status_code))


#Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'3',"192.0.0.1/32","192.0.0.2/32","0x0800","ETH_TYPE")
#Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'LOCAL',"192.0.0.2/32","192.0.0.1/32","0x0800","ETH_TYPE")

#Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'1',"192.0.0.2/32","192.0.0.1/32","0x0800","ETH_TYPE")
#Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'LOCAL',"192.0.0.1/32","192.0.0.2/32","0x0800","ETH_TYPE")



#Routing_rule_post("of:00009cebe831287a","65051","OUTPUT",'2',"192.0.0.1/32","192.0.0.3/32","0x0800","ETH_TYPE")
#Routing_rule_post("of:00009cebe831287a","65051","OUTPUT",'LOCAL',"192.0.0.3/32","192.0.0.1/32","0x0800","ETH_TYPE")

#Routing_rule_post_udp("of:0000e0cb4e9b78a2","65051","OUTPUT",'2',"192.0.0.3/32","192.0.0.1/32",'16000','17000',"0x0800","ETH_TYPE")
#Routing_rule_post_tcp("of:0000e0cb4e9b78a2","65051","OUTPUT",'2',"192.0.0.1/32","192.0.0.1/32",'16000','17000',"0x0800","ETH_TYPE")
#Routing_rule_post_udp_only_dst_port("of:0000e0cb4e9b78a2","65051","OUTPUT",'2',"192.0.0.2/32","192.0.0.1/32",'16000','17000',"0x0800","ETH_TYPE")
#Routing_rule_post_tcp_only_dst_port("of:0000e0cb4e9b78a2","65051","OUTPUT",'2',"192.0.0.4/32","192.0.0.1/32",'16000','17000',"0x0800","ETH_TYPE")

#Routing_rule_post("of:00009cebe83128b4","65051","OUTPUT",'LOCAL',"192.0.0.1/32","192.0.0.3/32","0x0800","ETH_TYPE")

