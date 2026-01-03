class Solution:
    def tribonacci(self, n: int) -> int:
        # top down
        def dp(i):
            if i <= 1:
                return i
            if i == 2:
                return 1
            
            if i not in memo:
                memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
            return memo[i]
        memo = {}
        return dp(n)
        # bottom up
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[n]

        