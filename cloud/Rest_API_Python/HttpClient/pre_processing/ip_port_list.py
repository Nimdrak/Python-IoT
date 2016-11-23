'''
Created on Jun 9, 2016

@author: controller
'''

##############################################


def ip_port_list_make(list):
#initialization
    for a in range(0,len(list)):
        f_write=open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table_flow/OVS"+str(a+1)+".txt",'w')
            
    
    for a in range(0,len(list)):
        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table/OVS"+str(a+1)+".txt",'r')
        line=f.readline()
        j=0
        for b in range(0,len(list[a])):
            result=line.split()
            for i in range(0,int(list[a][b][0])):
                j=j+1
                print j,result[1],60000+i
                f_write=open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table_flow/OVS"+str(a+1)+".txt",'a'  )
                data="%d\t%s\t%d\n" %(j, result[1], 60000+i)
                f_write.write(data)
    
    
            line=f.readline()
    

#available_requst_number=[[['7'], ['7'], ['7'], ['7'], ['80']], [['7'], ['7'], ['7'], ['7'], ['80']], [['7'], ['7'], ['7'], ['7'], ['80']], [['7'], ['7'], ['7'], ['7'], ['80']]]
#ip_port_list_make(available_requst_number)



