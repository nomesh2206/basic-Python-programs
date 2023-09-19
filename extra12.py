# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:38:32 2023

@author: a
"""

def fun(l,index,num):
    l1=[]
    for i in range(len(l)):
        if i==index:
            l1.append(num)
        else:
            l1.append(l[i])
            
    return l1

lst=[10,20,30,40]
print(fun(lst,2,5))
