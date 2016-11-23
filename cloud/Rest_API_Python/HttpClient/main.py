'''
Created on Mar 31, 2016

@author: nimdrak
'''

import function_allocation_REST
import function_controller_path_setting
#import function_link_sorting_output

import sys
 
import pre_processing.available_request
import pre_processing.ip_port_list
import pre_processing.function_making_information_link
import flow.function_making_REST_input_flow
import flow.function_allocation_REST_flow

import function_routing_rule_post
import dc_rule

if __name__ == '__main__':
    

# making information    
    index_vector=[0,0,0,0]
    request_vector=[0,0,0,0]
    
#    result=function_allocation_server.allocation_server_with_text_input(index_vector,sys.argv[1])
#    pre_processing.function_making_information.allocation_server_with_text_input(index_vector,'input.txt')    
    pre_processing.function_making_information_link.link_sorting_output_with_text_input('input.txt')     
    result=flow.function_making_REST_input_flow.allocation_server_with_text_input(request_vector, 'input.txt')
#    pre_processing.function_making_information.allocation_server_with_text_input(index_vector,sys.argv[1])    
#    pre_processing.function_making_information_link.link_sorting_output_with_text_input(sys.argv[1])     
#    result=flow.function_making_REST_input_flow.allocation_server_with_text_input(request_vector, sys.argv[1])
        
 

# available_request and making the list in terms of IP and port
    data_center=['1','2','3','4']
    available_requst_number=pre_processing.available_request.available_request_find(data_center)
    pre_processing.ip_port_list.ip_port_list_make(available_requst_number)


# controller to server path setting - using wirenetwork
    a=function_controller_path_setting.controller_path_setting(4)    
    for y in range(0,len(a)):
        for x in range(0,len(a[0])):
            print a[y][x]
            function_allocation_REST.function_main(a[y][x])

# controller to ovs path setting
#    data_center_id=['of:000000259006798c','of:00000025900b66fe','of:00000025900ca3f4','of:0000002590322dca']
#    for z in range(0,len(data_center_id)):
#        function_routing_rule_post.Routing_rule_post_only_src(data_center_id[z],"10000","OUTPUT",'NORMAL',"192.0.0.200/32","0x0800","ETH_TYPE")
#        function_routing_rule_post.Routing_rule_post_only_dst(data_center_id[z],"10000","OUTPUT",'NORMAL',"192.0.0.200/32","0x0800","ETH_TYPE")            
    dc_rule.for_dc()           
                
# flow allocation

    for x in range(0,len(result[0])):
        flow.function_allocation_REST_flow.function_main(result[0][x],result[1][x])  
        print result[0][x],result[1][x]
 #   print "Using servers are ",index_vector, " Using Requests are", request_vector

#    print '\n'
#    print "Adding flow rules are finished"
#    print '\n'
#    print "result is", result[0]
#    print result[1]




    

    