'''
Created on May 3, 2016

@author: cloud1
'''

def str_to_list(input_str):
    
    
    a=input_str[1:-2].split(',')
    list_temp= []
    for e in a:
        list_temp.append(e.strip()[1:-1])
    return list_temp

