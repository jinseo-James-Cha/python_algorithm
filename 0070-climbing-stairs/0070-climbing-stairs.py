class Solution:
    def climbStairs(self, n: int) -> int:
        # top down
        def dp(n):
            if n <= 2:
                return n

            if n in memo:
                return memo[n]
            
            memo[n] = dp(n-2) + dp(n-1)
            return memo[n]
        
        memo = {}
        return dp(n)