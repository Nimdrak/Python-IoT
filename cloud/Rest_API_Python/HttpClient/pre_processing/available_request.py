'''
Created on Jun 9, 2016

@author: controller
'''

##############################################



def available_request_find(input):

    available_flow_request_number=[]
    each_flow=[]
    
    for i in range(0,len(input)):
        
        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table_flow_number/OVS" + input[i] +".txt",'r')
        line=f.readline()
        
        while line:
            result=line.split()
            line=f.readline()
    #        print result
            each_flow.append(result)
            if not line:
                available_flow_request_number.append(each_flow)
                each_flow=[]
                break
        
    print available_flow_request_number
    return available_flow_request_number