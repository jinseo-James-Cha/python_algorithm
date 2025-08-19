class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # optimized bottom up
        prev = 0
        prev_prev = 0
        
        for i in range(2, len(cost) + 1):
            current = min(prev + cost[i-1], prev_prev + cost[i-2])
            prev_prev = prev
            prev = current
        return prev
        
#         # bottom up
#         dp = [0] * (len(cost) + 1)
        
#         for i in range(2, len(cost) + 1):
#             dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
#         return dp[len(cost)]
        
        # top down
#         def dp(i):
#             if i <= 1:
#                 return 0
            
#             if i not in memo:
#                 memo[i] = min(dp(i-2) + cost[i-2], dp(i-1) + cost[i-1])
            
#             return memo[i]
            
#         memo = {}
#         return dp(len(cost))