'''
Created on Mar 31, 2016

@author: nimdrak
'''

import function_allocation_routing_path
import function_routing_rule_post
import function_ovs_translation_from_number_to_id
import sys


if __name__ == '__main__':
    
    ##########################
    ####routing allocation####
    ##########################

    algo_output1 = []
    for a in range(1,len(sys.argv)):
        algo_output1.append(sys.argv[a])
    print algo_output1    
#    algo_output1 = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]    
#    algo_output1 = ['192.0.0.121/32','2','4','3','192.0.0.130/32']
    dst_port_list_algo_output=[]
    src_port_list_algo_output=[]

    dst_port_list_algo_output = function_allocation_routing_path.Allocation_routing_dst_port(algo_output1)
    src_port_list_algo_output = function_allocation_routing_path.Allocation_routing_src_port(algo_output1)
 

    print '\n'
    print '\n'    
    print '\n'
    print '##########################'
    print '####routing allocation####'
    print '##########################'
    print 'Result is'
    print 'Source ports are -->',src_port_list_algo_output
    print 'Destination ports are --> ',dst_port_list_algo_output
    



    
    ##########################
    #####OVSnumber->OVSid#####
    ##########################
    

    result_translation=[]
    for a in range(1,len(algo_output1)-1):
        result_translation.append('DEFAULT')

    
    for i in range(1,len(algo_output1)-1):
        result_translation[i-1]=function_ovs_translation_from_number_to_id.translation_from_num_to_id(algo_output1[i])

    print '\n'
    print '\n'    
    print '\n'
    print '##########################'
    print '####OVSnumber--->OVSid####'
    print '##########################'
    print result_translation
#    print result_translation[0][1]

    


    #########################
    ####routing_rule_post####
    #########################
    
    
    #using for ~ in range ~





############################################################################################
##### Device_id, Priority, Type, Out_port, Src_IP, Dst_IP, ARP_or_IP, ARP_or_IP_Type): #####
############################################################################################

    inputs=["of:000000606eb248fb","1","OUTPUT","1","192.0.0.198/32","192.0.0.202/32","0x0800","ETH_TYPE"]

####################
##### Variable #####
####################

#    print 'Source ports are -->',src_port_list_algo_output
#    print 'Destination ports are --> ',dst_port_list_algo_output
#    print result_translation
print '\n'
print '\n'
print 'Src HOST is',algo_output1[0]
print 'Dst HOST is',algo_output1[len(algo_output1)-1]
print '\n'
print '\n'

for a in range(1,len(algo_output1)-1):
#    print a
    
    print 'OVS name is',result_translation[a-1][0] # OVS name
    print 'OVS name ID IS',result_translation[a-1][1] # OVS name's ID
    print 'OVS name IP IS',result_translation[a-1][2] # OVS name's IP
    print 'OVS name <-(src)',src_port_list_algo_output[a-1] #OVS name's <-
    print 'OVS name <-(dst)',dst_port_list_algo_output[a-1] #OVS name's ->
    print '\n'

#############################
##### DST FLOW RULE ADD #####
#############################

for a in range(1,len(algo_output1)-1):
#    print a
        
    function_routing_rule_post.Routing_rule_post(result_translation[a-1][1],"65250","OUTPUT",dst_port_list_algo_output[a-1],algo_output1[0],algo_output1[len(algo_output1)-1],"0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post_arp_drop(result_translation[a-1][1], "65250")
    
#############################
##### SRC FLOW RULE ADD #####
#############################

for a in range(1,len(algo_output1)-1):
#    print a
    function_routing_rule_post.Routing_rule_post(result_translation[a-1][1],"65250","OUTPUT",src_port_list_algo_output[a-1],algo_output1[len(algo_output1)-1],algo_output1[0],"0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post_arp_drop(result_translation[a-1][1], "65250")





#   function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")



####function_routing_rule_post.Routing_rule_post(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7])
    
#function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")
#function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'3',"192.0.0.101/32","192.0.0.100/32","0x0800","ETH_TYPE")

#function_routing_rule_post.Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")    
#function_routing_rule_post.Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'3',"192.0.0.101/32","192.0.0.100/32","0x0800","ETH_TYPE")


    