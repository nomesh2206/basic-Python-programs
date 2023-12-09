class Solution:
    def prime_factors(self, n):
        factors = []
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1

        return factors
        
    def digit_sum(self, n):
        return sum(int(digit) for digit in str(n))
    
    def is_smith_number(self, n):
        factors = self.prime_factors(n)
        digit_sum_original = self.digit_sum(n)
        digit_sum_factors = sum(self.digit_sum(factor) for factor in factors)
        
        return digit_sum_original == digit_sum_factors
