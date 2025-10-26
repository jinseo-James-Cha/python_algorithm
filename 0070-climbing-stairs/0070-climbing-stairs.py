class Solution:
    def climbStairs(self, n: int) -> int:
        # top down
        @cache
        def dp(i):
            if i <= 2:
                return i
            
            return dp(i-2) + dp(i-1)
        
        return dp(n)
