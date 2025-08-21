class Solution:
    def numWays(self, n: int, k: int) -> int:
        # bottom up constant space
        if n <= 2:
            return k**n
        
        one_back = k * k
        two_back = k
        for i in range(3, n+1):
            current = (k-1) * one_back + (k-1) * two_back
            two_back = one_back
            one_back = current
        return one_back




        # bottom up
        if n == 1:
            return k

        dp = [0] * (n+1)
        dp[1] = k
        dp[2] = k * k

        for i in range(3, n+1):
            dp[i] = (k-1) * dp[i-1] + (k-1) * dp[i-2]
        
        return dp[n]


        # Top down
        def dp(i):
            if i <= 2:
                return k**i
            if i not in memo:
                memo[i] = (k-1) * dp(i-1) + (k-1) * dp(i-2)
            
            return memo[i]
            
        memo = {}
        return dp(n)