'''
Created on May 9, 2016

@author: nimdrak
'''
import os
import operator
import sys

#dirname1='/home/controller/IoT/normal_packet/output'
def search(dirname):


    filenames = os.listdir(dirname)
    #for filename in filenames:
    #    full_filename=os.path.join(dirname, filename)
    #    ext = os.path.splitext(full_filename)[-1]                           
    #    if ext == '.txt':
            #print(full_filename)
            
    file_name=[]
    data_vector=[]
    all_data_vector=[]
    sum_data_vector=[]
    time_vector=[]
    data_number=0
    
    
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
    #        print filename
            if 'bw' in filename:
                print("%s %s" % (path, filename))
                
                file_name.append(filename)
    
    #            print path+'/'+filename
                bw_data=open(path+'/'+file_name[data_number],'r')
                
                
                line=bw_data.readline()
                result=line.split()
                data_vector.append(result)
    #            print data_vector
                
                while line:
                    line=bw_data.readline()
                    result=line.split()
                    if result==[]:
                        break
                    data_vector.append(result)
                    
                data_number=data_number+1    
                #print data_vector
                all_data_vector.append(data_vector)
                data_vector=[]
            
    
    
    for i in range(0,len(all_data_vector[0])):
        sum_data_vector.append(0)
    
    
    
    for j in range(0,len(all_data_vector[0])):
        for i in range(0,data_number):
            sum_data_vector[j]=sum_data_vector[j]+(float(all_data_vector[i][j][0]))/5
    
    print sum_data_vector
    
    
    f_sum_result=open(dirname+'/'+'sum_result.txt','w')
    
    for i in range(0,len(all_data_vector[0])):
        data = str(sum_data_vector[i]) + '\n'
        f_sum_result.write(data)
        
    f_sum_result.close()
        

search(dirname1)