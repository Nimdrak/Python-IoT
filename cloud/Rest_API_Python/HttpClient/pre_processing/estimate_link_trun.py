'''
Created on Oct 17, 2016

@author: controller
'''

'''

This code estimate the amount of specific link traffic 
using mean and variance of each flow in that link

For this, This code read the text files "output_including_link" and "input_mean"
in output_txt folder

'''

import function_string_to_list

f_mean = open("/home/controller/IoT/input_mean_trun.txt",'r')
f_link = open("/home/controller/IoT/output_txt/output_including_link.txt",'r')


line1=f_mean.readline()
list_temp1 = line1.split() 

line2=f_link.readline()
list_temp2 = function_string_to_list.str_to_list(line2) 


sum_mean_link_1 = 0
variance_square_sum_link_1 = 0

sum_mean_link_2 = 0
variance_square_sum_link_2 = 0

sum_mean_link_3 = 0
variance_square_sum_link_3 = 0

sum_mean_link_4 = 0
variance_square_sum_link_4 = 0

sum_mean_link_5 = 0
variance_square_sum_link_5 = 0

number_of_request=0
simple_sum_mean=0


##########################
###### Link Output #######
##########################

#########################
#### First Line Case ####
#########################

list_temp = list_temp1 + list_temp2
print list_temp


for i in range(len(list_temp2)):
    if list_temp[2+i] == '1':
        sum_mean_link_1 += float(list_temp[0])
        variance_square_sum_link_1 += pow(float(list_temp[1]),2)       
    
    elif list_temp[2+i] == '2':
        sum_mean_link_2 += float(list_temp[0])
        variance_square_sum_link_2 += pow(float(list_temp[1]),2)

        
    elif list_temp[2+i] == '3':
        sum_mean_link_3 += float(list_temp[0])
        variance_square_sum_link_3 += pow(float(list_temp[1]),2)

    elif list_temp[2+i] == '4':
        sum_mean_link_4 += float(list_temp[0])
        variance_square_sum_link_4 += pow(float(list_temp[1]),2)

    elif list_temp[2+i] == '5':
        sum_mean_link_5 += float(list_temp[0])
        variance_square_sum_link_5 += pow(float(list_temp[1]),2)

simple_sum_mean += float(list_temp[0])
number_of_request+=1

while line1:

    line1=f_mean.readline()
    list_temp1 = line1.split() 
    line2=f_link.readline()
    list_temp2 = function_string_to_list.str_to_list(line2) 
    list_temp = list_temp1 + list_temp2
    print list_temp
    
    if list_temp==['']:
        break
        

    number_of_request+=1    
    simple_sum_mean += float(list_temp[0])
    
    for i in range(len(list_temp2)):
        if list_temp[2+i] == '1':
            sum_mean_link_1 += float(list_temp[0])
            variance_square_sum_link_1 += pow(float(list_temp[1]),2)       
        
        elif list_temp[2+i] == '2':
            sum_mean_link_2 += float(list_temp[0])
            variance_square_sum_link_2 += pow(float(list_temp[1]),2)
    
            
        elif list_temp[2+i] == '3':
            sum_mean_link_3 += float(list_temp[0])
            variance_square_sum_link_3 += pow(float(list_temp[1]),2)
    
        elif list_temp[2+i] == '4':
            sum_mean_link_4 += float(list_temp[0])
            variance_square_sum_link_4 += pow(float(list_temp[1]),2)
    
        elif list_temp[2+i] == '5':
            sum_mean_link_5 += float(list_temp[0])
            variance_square_sum_link_5 += pow(float(list_temp[1]),2)
                
                
print(sum_mean_link_1)
print(sum_mean_link_2)
print(sum_mean_link_3)
print(sum_mean_link_4)
print(sum_mean_link_5)



f_result=open("/home/controller/IoT/output_txt/sum_mean_link_trun.txt",'w')
data= str(sum_mean_link_1) + ',' + str(variance_square_sum_link_1)
f_result.write(data)
f_result.write('\n')

data= str(sum_mean_link_2) + ',' + str(variance_square_sum_link_2)
f_result.write(data)
f_result.write('\n')

data= str(sum_mean_link_3) + ',' + str(variance_square_sum_link_3)
f_result.write(data)
f_result.write('\n')

data= str(sum_mean_link_4) + ',' + str(variance_square_sum_link_4)
f_result.write(data)
f_result.write('\n')

data= str(sum_mean_link_5) + ',' + str(variance_square_sum_link_5)
f_result.write(data)
f_result.write('\n')

data='The number of total request is ' + str(number_of_request)
f_result.write(data)
f_result.write('\n')

data='The simply total sum of mean is ' + str(simple_sum_mean)
f_result.write(data)
f_result.write('\n')


f_result.close()








