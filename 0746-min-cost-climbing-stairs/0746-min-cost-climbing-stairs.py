class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp bottom up
        prev_prev = prev = 0
        for i in range(2, len(cost) + 1):
            curr = min(prev + cost[i - 1], prev_prev + cost[i - 2])
            
            prev_prev = prev
            prev = curr
        return prev

        # dp top down
        def dp(i):
            if i <= 1:
                return 0

            if i not in memo:
                memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))