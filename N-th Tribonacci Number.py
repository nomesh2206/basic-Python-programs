def nthTribonacci(n):
    dp = [-1]*21
    dp[0] = dp[1] = 0
    dp[2] = 1
    def tribo(n):
        if(n==0 or n==1):
            return 0
        if(n==2):
            return 1
        if(dp[n]!=-1):
            return dp[n]
        nthNumber = nthTribonacci(n-1)+nthTribonacci(n-2)+nthTribonacci(n-3)
        dp[n] = nthNumber
        return nthNumber
    return tribo(n)
