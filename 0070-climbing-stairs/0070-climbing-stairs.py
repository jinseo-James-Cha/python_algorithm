class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1) :
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

        # top down
        # def dp(n):
        #     if n <= 2:
        #         return n

        #     if n in memo:
        #         return memo[n]
            
        #     memo[n] = dp(n-2) + dp(n-1)
        #     return memo[n]
        
        # memo = {}
        # return dp(n)