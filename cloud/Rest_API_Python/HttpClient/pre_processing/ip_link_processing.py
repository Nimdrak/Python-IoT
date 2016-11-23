'''
Created on May 6, 2016

@author: cloud1
'''

import function_string_to_list


#######################
#### load two file ####
#######################
f_ip = open("/home/byounguklee/mininet/con_python/output_txt/output_including_ip.txt",'r')
f_link = open("/home/byounguklee/mininet/con_python/output_txt/output_including_link.txt",'r')


line1=f_ip.readline()
list_temp1 = function_string_to_list.str_to_list(line1) 

line2=f_link.readline()
list_temp2 = function_string_to_list.str_to_list(line2) 



#### first line case
final_output=[]
output=[]


output.append(list_temp1[0])
output.append(list_temp1[len(list_temp1)-1])
for x in range(0,len(list_temp2)):
    output.append(list_temp2[x])       
final_output.append(output)


print output
#### after first line
while line1:
    output=[]

    line1=f_ip.readline()
    list_temp1 = function_string_to_list.str_to_list(line1)

    line2=f_link.readline()
    list_temp2 = function_string_to_list.str_to_list(line2) 

    if list_temp2[0]=='':
        break
    
    
    output.append(list_temp1[0])
    output.append(list_temp1[len(list_temp1)-1])
    
    for x in range(0,len(list_temp2)):
        output.append(list_temp2[x])     
    
    print output
    final_output.append(output)
    output=[]


############ Possible problem
f_allo_result=open("/home/byounguklee/mininet/con_python/output_txt/output_ip_link.txt",'w')
for i in range(0,len(final_output)):
    for j in range(0,2)    :
        data = str(final_output[i][j]).strip()[0:-3] + ','
        f_allo_result.write(data)
    
    if len(final_output[i]) != 2:
    
        for j in range(2,len(final_output[i])-1):
            data = str(final_output[i][j]) + ','
            f_allo_result.write(data)

        data = str(final_output[i][len(final_output[i])-1])
        f_allo_result.write(data)

     
    else:
        data = str(final_output[i][len(final_output[i])-1])
        f_allo_result.write(data)
  
    f_allo_result.write('\n')    
    
f_allo_result.close()
