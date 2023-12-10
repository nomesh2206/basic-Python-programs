class Solution:
    @staticmethod
    def smithNum(n):
        if Solution.digit_sum(n) == Solution.prime_factor_sum(n):
            return 1
        return 0
    
    @staticmethod
    def prime_factor_sum(n):
        count = 0
        res = 0
        i = 2
        while n > 1:
            if n % i == 0:
                count += 1
            if n % i == 0:
                if i > 10:
                    res += Solution.digit_sum(i)
                else:
                    res += i
                n = n // i
            else:
                i += 1 
        return res if count > 1 else 0

    @staticmethod
    def digit_sum(x):
        res = 0
        while x != 0:
            res += x % 10
            x = x // 10
        return res
