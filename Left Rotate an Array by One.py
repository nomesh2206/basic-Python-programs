from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    x = arr[0]
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = x

    return arr

input : n = 5, arr = [1,2,3,4,5]
output : arr = [2,3,4,5,1]
