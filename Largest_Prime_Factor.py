class Solution:
    def largestPrimeFactor(self, N):
        i = 2
        while(i*i<=N):
            if (N%i == 0):
                N = int(N/i)
            else:
                i = i + 1
        return N
