'''
Created on Mar 24, 2016

@author: nimdrak
'''

algo_output = ['100','1','2','101']


##########################
##### Initialization #####
##########################

src_port_list =[]
dst_port_list =[]

for a in range(1,len(algo_output)-1):
    src_port_list.append('DEFAULT')
    dst_port_list.append('DEFAULT')
print src_port_list
print dst_port_list

    
#################################
##### forwarding allocation #####
#################################


for x in range(1,len(algo_output)-1):

    current = algo_output[x]
    ahead = algo_output[x-1]
    after = algo_output[x+1]
    print '\n'
    print 'current:',current,',ahead:',ahead,',after:',after

    f = open("/home/cloud1/workspace/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
    line=f.readline()

    while line:
        result=line.split()
        line=f.readline()
        if not line:
            break

        if result[0]==ahead:
            src_port_list[x-1] = result[2]
            print current,src_port_list[x-1] # AHEAD HOST, CANNOT CATCH

            
        if result[0]==after:
            dst_port_list[x-1] =result[2]
            print current,dst_port_list[x-1] # DST HOST, CANNOT CATCH



print '\n'

print '####middle point check####'
print src_port_list
print dst_port_list
print '\n'

    

for x in range(1,len(algo_output)-1):

    current = algo_output[x]
    ahead = algo_output[x-1]
    after = algo_output[x+1]
    

    f = open("/home/cloud1/workspace/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
    line=f.readline()

    if src_port_list[x-1] =='DEFAULT':

        while line:
            ## excepting first line
            line=f.readline()
            result=line.split()   
      

            if result==[]: ## why?
                break

            if result[0]=='HOST':
                src_port_list[x-1] = result[2]
                print current,ahead,after,'HOST case',src_port_list[x-1]

               
for x in range(1,len(algo_output)-1):

    current = algo_output[x]
    ahead = algo_output[x-1]
    after = algo_output[x+1]
    

    f = open("/home/cloud1/workspace/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
    line=f.readline()

    if dst_port_list[x-1] =='DEFAULT':

        while line:
            ## excepting first line
            line=f.readline()
            result=line.split()           
            if not line:
                break

            if result[0]=='HOST':
                dst_port_list[x-1] = result[2]
                print current,ahead,after,'HOST case',dst_port_list[x-1]



##################################
##### Port Forwarding output #####
##################################

                
print '\n'
print '\n'
print '####OVS src_port_list in order ####'
print src_port_list

print '####OVS dst_port_list in order ####'
print dst_port_list

    
            