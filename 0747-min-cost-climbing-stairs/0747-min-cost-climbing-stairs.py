class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            # if i < 0:
            #     return 0
            if i == 0 or i == 1:
                return cost[i]
            if i not in memo:
                memo[i] = cost[i] + min(dp(i-1), dp(i-2))
            return memo[i]

        # 마지막 계단(len(cost)-1) 또는 그 전 계단(len(cost)-2)에서 한 번에 올라갈 수 있으므로
        return min(dp(len(cost)-1), dp(len(cost)-2))

        # 1step or 2step -> minimize total cost
        # dp[len(cost)] -> top of the floor -> the answer

        # 1. bottom-up / tabulation
        # dp = [0] * (len(cost) + 1) # for the arrival 
        # # index 0, 1 are available to start, so its 0
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        # return dp[-1]

        # 2. top-down / memoization
        # def cal_cost(i):
        #     # first and second can be starting point, so value 0
        #     if i <= 1:
        #         return 0
            
        #     # if already calculated, using memoization
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = min(cal_cost(i-2) + cost[i-2], cal_cost(i-1) + cost[i-1])
        #     return memo[i]
        # memo = {}
        # return cal_cost(len(cost))