'''
Created on May 3, 2016

@author: nimdrak
'''

import sys


index_vector=[0,0,0,0]



def allocation_server(index_vector,result = [], *args):
 
#################################
#### Get DC that need server ####
#################################


    src_ovs=result[0]
    dst_ovs=result[len(result)-1]

    need_server_ovs=[]  ## We need to take server from these OVS
    need_server_ovs.append(result[0])
    need_server_ovs.append(result[len(result)-1])

#    print "Need server OVS is " , need_server_ovs
#    print '\n'



#################################
#### Calculate server per DC ####
#################################

#Get number of host from OVS1 server table
    number_server = 0
    f_cal = open("/home/controller/IoT/cloud/Rest_API_Python/HttpClient/server_table/OVS1.txt",'r')
    line_cal=f_cal.readline()

    while line_cal:
        result_cal=line_cal.split()
        line_cal=f_cal.readline()
        number_server=number_server+1

    number_server = number_server # CAUTION Because table has additional one line
#    print "Server number is " + str(number_server)
#    print '\n'

#    if number_server!=4:
#            print >> sys.stderr, "Check the table entry enter"            


##################################################
#### Check whether Data-center is full or not ####
##################################################

#    print 'Check whether Data-center is full or not'

#    if index_vector[int(src_ovs)-1]==number_server: # Because vector numbering starts 0, we use -1
#            print >> sys.stderr, "Because DC" +str(src_ovs)+"is full ",", Admission control is impossible"
#    if index_vector[int(dst_ovs)-1]==number_server:
#            print >> sys.stderr, "Because DC" +str(dst_ovs)+"is full ",", Admission control is impossible"            



##############################################
#### Allocation of server at requested DC ####
##############################################


    Allocatio_result=[]

    for x in range(0,len(need_server_ovs)):
        
    #First, we need to read need server OVS's table
        f_algo = open("/home/controller/IoT/cloud/Rest_API_Python/HttpClient/server_table/"+"OVS"+need_server_ovs[x]+".txt",'r')

    #Second, we take the server that have number, index + 1
        line_algo=f_algo.readline()
        for y in range(0,index_vector[int(need_server_ovs[x]) -1] +1): #-1 is result of Python vector numbering and +1 is result of Python range
            result_algo=line_algo.split()
            line_algo=f_algo.readline()
            
            if result_algo[0] == str(index_vector[int(need_server_ovs[x])-1]+1): #check server number == index number of that ovs +1
                Allocatio_result.append(result_algo[1])
                index_vector[int(need_server_ovs[x])-1] = index_vector[int(need_server_ovs[x])-1] + 1 # After allocation, index number increases by 1

    print "Allocation result is ", Allocatio_result            



#############################################
#### Make result form of allocation REST ####
#############################################


    Final_result=[]
    Final_result.append(Allocatio_result[0])
    for x in range(0,len(result)):
        Final_result.append(result[x])
    Final_result.append(Allocatio_result[1])

    print "Allocation result of request form is ", Final_result
    return Final_result   
    


############################################
#### allocation with text input version ####
############################################

    
def allocation_server_with_text_input(index_vector,file_input_name):

#read algorithm's output from text file       
 
    f = open("/home/controller/IoT/" + file_input_name,'r')

    list_result = [] # list for binding all itput
    allo_result = [] # list for binding all output
    
    line=f.readline()
    
    while line:
        result=line.split()
        line=f.readline()
        list_result.append(result) # binding input in list_result
        
        if not line:
#            print list_result
            break
  
    print list_result
#make output from list_result
    for z in range(0,len(list_result)):
        print '\n'
        print '################'
        print "Input number is " + str(z+1)
        print '################'
        print '\n'
        
        output_allo = allocation_server(index_vector,list_result[z])
        allo_result.append(output_allo) # binding input in output_result
    
    print '\n'
    print '################'
    print "Using server number is ", index_vector
    print "All output is ", allo_result

#write output in txt file    
    f_allo_result=open("/home/controller/IoT/output_txt/output_including_ip.txt",'w')
    for i in range(0,len(allo_result)):
        data = str(allo_result[i]) + '\n'
        
        f_allo_result.write(data)
    f_allo_result.close()
    
    


    return allo_result


#result=allocation_server_with_text_input(index_vector,'input.txt')
#print result