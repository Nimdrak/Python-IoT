'''
Created on May 3, 2016

@author: cloud1
'''
import function_string_to_list

#######################
#### load two file ####
#######################
f_ip = open("/home/controller/IoT/output_txt/output_including_ip.txt",'r')
f_mean = open("/home/controller/IoT/input_mean.txt",'r')


line1=f_ip.readline()
list_temp1 = function_string_to_list.str_to_list(line1)
line2=f_mean.readline()
result=line2.split()


#### first line case
final_output=[]
output=[]


output.append(list_temp1[0])
output.append(list_temp1[len(list_temp1)-1])
output.append(result[0])
output.append(result[1])       
final_output.append(output)

print output

#### after first line
while line1:
    output=[]

    line1=f_ip.readline()
    list_temp1 = function_string_to_list.str_to_list(line1)
    line2=f_mean.readline()
    result=line2.split()

    if result ==[]:
        break
    
    
    output.append(list_temp1[0])
    output.append(list_temp1[len(list_temp1)-1])
    output.append(result[0])
    output.append(result[1])    
    
    print output
    final_output.append(output)
    output=[]
    

    
print final_output


f_allo_result=open("/home/controller/IoT/output_txt/output_ip_mean_193.txt",'w')
for i in range(0,len(final_output)):
    for j in range(0,len(final_output[i])-2)    :
        data = '193'+str(final_output[i][j]).strip()[3:-3] + ','
        f_allo_result.write(data)
    
    for j in range(2,len(final_output[i])-1):
        data = str(final_output[i][j]) + ','
        f_allo_result.write(data)
        
    for j in range(3,len(final_output[i])):
        data = str(final_output[i][j])
        f_allo_result.write(data)        
    
    f_allo_result.write('\n')    
f_allo_result.close()