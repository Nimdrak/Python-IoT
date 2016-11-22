'''
Created on May 3, 2016

@author: nimdrak
'''

import sys


index_vector=[0,0,0,0]



def allocation_server(index_vector,result = [], *args):
 
 
    need_server_ovs=[] 
    need_server_ovs.append(result[0])
    need_server_ovs.append(result[len(result)-1])


    Allocation_result=[]
    Allocation_result_port=[]

    for x in range(0,len(need_server_ovs)):
        
    #First, we need to read need server OVS's table
        f_algo = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table_flow/"+"OVS"+need_server_ovs[x]+".txt",'r')

    #Second, we take the server that have number, index + 1
        line_algo=f_algo.readline()
        for y in range(0,index_vector[int(need_server_ovs[x]) -1] +1): #-1 is result of Python vector numbering and +1 is result of Python range
            result_algo=line_algo.split()
            line_algo=f_algo.readline()
            if result_algo[0] == str(index_vector[int(need_server_ovs[x])-1]+1): #check server number == index number of that ovs +1
                Allocation_result.append(result_algo[1])
                Allocation_result_port.append(result_algo[2])
                index_vector[int(need_server_ovs[x])-1] = index_vector[int(need_server_ovs[x])-1] + 1 # After allocation, index number increases by 1

    print "Allocation result is ", Allocation_result,Allocation_result_port            



#############################################
#### Make result form of allocation REST ####
#############################################


    Final_result=[]
    Final_result_port=[]
    Final_result.append(Allocation_result[0])
    for x in range(0,len(result)):
        Final_result.append(result[x])
    Final_result.append(Allocation_result[1])
    Final_result_port.append(Allocation_result_port[0])
    Final_result_port.append(Allocation_result_port[1])
#    print "Allocation result of request form is ", Final_result
    return Final_result,Final_result_port
    
#aa=allocation_server(index_vector,['1','2'])
#print aa[0]

############################################
#### allocation with text input version ####
############################################

    
def allocation_server_with_text_input(index_vector,file_input_name):

#read algorithm's output from text file       
 
    f = open("/home/byounguklee/mininet/con_python/" + file_input_name,'r')

    list_result = [] # list for binding all itput
    allo_result = [] # list for binding all output
    allo_result_port = []
    
    line=f.readline()
    
    while line:
        result=line.split()
        line=f.readline()
        list_result.append(result) # binding input in list_result
        
        if not line:
#            print list_result
            break
  

#make output from list_result
    for z in range(0,len(list_result)):
        print '\n'
        print '################'
        print "Input number is " + str(z+1)
        print '################'
        print '\n'
        output_allo = allocation_server(index_vector,list_result[z])
        allo_result.append(output_allo[0]) # binding input in output_result
        allo_result_port.append(output_allo[1]) # binding input in output_result

    
    print '\n'
    print '################'
    print "Using server number is ", index_vector
    print "All output is ", allo_result,allo_result_port

#write output in txt file    
    f_allo_result=open("/home/byounguklee/mininet/con_python/output_txt/output_including_ip.txt",'w')
    for i in range(0,len(allo_result)):
        data = str(allo_result[i]) + '\n'
        
        f_allo_result.write(data)
    f_allo_result.close()
    
    f_allo_result_port=open("/home/byounguklee/mininet/con_python/output_txt/output_port.txt",'w')
    for i in range(0,len(allo_result_port)):
        data = str(allo_result_port[i][0])+ ',' +str(allo_result_port[i][1])+'\n'
        f_allo_result_port.write(data)
    f_allo_result_port.close()
   

    return allo_result,allo_result_port

#result=allocation_server_with_text_input(index_vector,'input.txt')
#print result