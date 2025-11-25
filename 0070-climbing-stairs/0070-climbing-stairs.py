class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up dp
        if n <= 2:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]


        
        # top down dp
        def dp(i):
            if i <= 2:
                return i
            
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        memo = {}
        return dp(n)