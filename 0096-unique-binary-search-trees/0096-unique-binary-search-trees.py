class Solution:
    def numTrees(self, n: int) -> int:
        # bottom up
        dp = [0] * (n+1)
        dp[0],dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
    
        return dp[n]




        # top down
        def dp(n):
            if n == 0:
                return 1
            if n <= 2:
                return n
            
            if n not in memo:
                total = 0
                for i in range(1, n+1):
                    left = dp(i-1)
                    right = dp(n-i)
                    total += left*right
                memo[i] = total    
            return memo[n]
        
        memo = {}
        return dp(n)