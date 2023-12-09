import math
class Solution:
    def isPrime(self, x: int):
        if x==1:
            return False
        elif x==2:
            return True
    
        for i in range(2, int(math.sqrt(x)) + 1):
            if(x%i==0):
                return False
    
        return True
    
    def minNumber(self, arr,n):
        sum = 0
        for i in range (n):
            sum += arr[i]
    
        if (self.isPrime(sum)):
            return 0
    
        for j in range(sum+1, 2*sum+1, 1):
            if (self.isPrime(j)):
                return j-sum
    
        return 0
