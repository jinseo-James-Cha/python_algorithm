class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1step or 2step -> minimize total cost
        # dp[len(cost)] -> top of the floor -> the answer

        # 1. bottom-up / tabulation
        dp = [0] * (len(cost) + 1) # for the arrival 
        # index 0, 1 are available to start, so its 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[-1]