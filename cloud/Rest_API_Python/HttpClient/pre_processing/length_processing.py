'''
Created on May 6, 2016

@author: cloud1
'''

f_length = open("/home/controller/IoT/output_txt/link_length.txt",'r')

line1=f_length.readline()    
a=line1[1:-1].split(',')
for i in range(0,len(a)):
    a[i]=a[i].strip()

print a



f_input_length=open("/home/controller/IoT/output_txt/output_link_length.txt",'w')
for i in range(0,len(a)-1):
    data=str(a[i]) + ','
    f_input_length.write(data)
f_input_length.write(str(a[len(a)-1]))
    

