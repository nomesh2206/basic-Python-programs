# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:18:59 2023

@author: a
"""

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

arr = [10, 4, 5, 8, 9, 7, 55, 22, 6]
y = search(arr, 11)
print(f"number at index {y + 1}")