class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # n rows houses
        # color 0red, 1blue, 2green
        # adjacent no same color

        # state
        # days
        # prev color ?
        
        # top down
        n = len(costs)
        def dp(i, color):
            total_cost = costs[i][color]
            if (i, color) not in memo:
                if i < len(costs) - 1:
                    if color == 0:
                        total_cost += min(dp(i+1, 1), dp(i+1, 2))
                    elif color == 1:
                        total_cost += min(dp(i+1, 0), dp(i+1, 2))
                    else:
                        total_cost += min(dp(i+1, 0), dp(i+1, 1))
                memo[(i, color)] = total_cost

            return memo[(i, color)]
        
        memo = {}
        return min(dp(0, 0), dp(0,1), dp(0, 2))

