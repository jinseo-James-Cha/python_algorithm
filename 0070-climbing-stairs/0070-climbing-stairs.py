class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
        
        
        # top down
        @cache
        def dp(i):
            if i <= 2:
                return i
            
            return dp(i-2) + dp(i-1)
        
        return dp(n)
