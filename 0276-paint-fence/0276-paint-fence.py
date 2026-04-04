class Solution:
    def numWays(self, n: int, k: int) -> int:
        # bottom up constant space
        # if n <= 2:
        #     return k**n
        
        # one_back = k * k
        # two_back = k
        # for i in range(3, n+1):
        #     current = (k-1) * one_back + (k-1) * two_back
        #     two_back = one_back
        #     one_back = current
        # return one_back




        # bottom up
        if n == 1:
            return k
        
        dp = [0] * (n+1)
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n+1):
            dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)

        return dp[n]



        # Counting DP - Top down
        # possibilities + possibilities => my possibilities
        # what is my current possibilities?
        # 1. any different colors with right prev color => dp(i-1) * (k-1)
        # 2. the same color with prev color=> different colors with 2 prev post => dp(i-2) * (k-1)
        def dp(i):
            if i <= 2:
                return k**i
            if i not in memo:
                memo[i] = (k-1) * dp(i-1) + (k-1) * dp(i-2)
            
            return memo[i]
            
        memo = {}
        return dp(n)