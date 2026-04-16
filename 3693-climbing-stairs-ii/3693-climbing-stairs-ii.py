class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def dp(i):
            if i == 0:
                return 0
            
            if i not in memo:
                res = float('inf')
                if i >= 1:
                    res = min(res, dp(i-1) + 1**2)
                if i >= 2:
                    res = min(res, dp(i-2) + 2**2)
                if i >= 3:
                    res = min(res, dp(i-3) + 3**2)

                memo[i] = res + costs[i-1]
            return memo[i]
        memo = {}
        return dp(n)