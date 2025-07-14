class Solution:
    def climbStairs(self, n: int) -> int:
        # v2: bottom-up
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        # v1: top-down -> TLE
        # memo = {}

        # if n <= 2:
        #     return n
        # if n in memo:
        #     return memo[n]
        
        # memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # return memo[n] 
        

