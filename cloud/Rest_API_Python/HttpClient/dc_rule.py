'''
Created on Jun 12, 2016

@author: controller
'''

import function_routing_rule_post

def for_dc():
    data_center_id=['of:000000259006798c','of:00000025900b66fe','of:00000025900ca3f4','of:0000002590322dca']
    
    function_routing_rule_post.Routing_rule_post('of:000000259006798c',"65400","OUTPUT",'LOCAL',"192.0.0.200/32","192.0.0.1/32","0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post_only_dst('of:000000259006798c',"65400","OUTPUT",'4',"192.0.0.200/32","0x0800","ETH_TYPE")
    
    
    
    function_routing_rule_post.Routing_rule_post('of:000000259006798c',"65400","OUTPUT",'3',"192.0.0.200/32","192.0.0.2/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'LOCAL',"192.0.0.200/32","192.0.0.2/32","0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'2',"192.0.0.2/32","192.0.0.200/32","0x0800","ETH_TYPE")
    
    
    
    
    function_routing_rule_post.Routing_rule_post('of:000000259006798c',"65400","OUTPUT",'3',"192.0.0.200/32","192.0.0.3/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'4',"192.0.0.200/32","192.0.0.3/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900ca3f4',"65400","OUTPUT",'LOCAL',"192.0.0.200/32","192.0.0.3/32","0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post('of:00000025900ca3f4',"65400","OUTPUT",'6',"192.0.0.3/32","192.0.0.200/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'2',"192.0.0.3/32","192.0.0.200/32","0x0800","ETH_TYPE")
    
    
    
    
    function_routing_rule_post.Routing_rule_post('of:000000259006798c',"65400","OUTPUT",'3',"192.0.0.200/32","192.0.0.4/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'4',"192.0.0.200/32","192.0.0.4/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900ca3f4',"65400","OUTPUT",'5',"192.0.0.200/32","192.0.0.4/32","0x0800","ETH_TYPE")
    
    
    function_routing_rule_post.Routing_rule_post('of:0000002590322dca',"65400","OUTPUT",'LOCAL',"192.0.0.200/32","192.0.0.4/32","0x0800","ETH_TYPE")
    function_routing_rule_post.Routing_rule_post('of:0000002590322dca',"65400","OUTPUT",'2',"192.0.0.4/32","192.0.0.200/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900ca3f4',"65400","OUTPUT",'6',"192.0.0.4/32","192.0.0.200/32","0x0800","ETH_TYPE")
    
    function_routing_rule_post.Routing_rule_post('of:00000025900b66fe',"65400","OUTPUT",'2',"192.0.0.4/32","192.0.0.200/32","0x0800","ETH_TYPE")


            
                    
for_dc()                