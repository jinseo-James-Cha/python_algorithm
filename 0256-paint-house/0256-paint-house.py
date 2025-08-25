class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # n rows houses
        # color 0red, 1blue, 2green
        # adjacent no same color

        # state
        # days
        # prev color 

        # bottom up optimization
        n = len(costs)
        prev_row = [x for x in costs[0]]
        for i in range(1, n):
            current_row = costs[i][:]
            
            current_row[0] += min(prev_row[1], prev_row[2])
            current_row[1] += min(prev_row[0], prev_row[2])
            current_row[2] += min(prev_row[0], prev_row[1])

            prev_row = current_row

        return min(prev_row)


        # bottom up
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1, n):
            for j in range(3):
                total_cost = costs[i][j]
                if j == 0:
                    total_cost += min(dp[i-1][1], dp[i-1][2])
                elif j == 1:
                    total_cost += min(dp[i-1][0], dp[i-1][2])
                else:
                    total_cost += min(dp[i-1][0], dp[i-1][1])
                dp[i][j] = total_cost
        
        return min(dp[n-1])




        
        # top down
        n = len(costs)
        def dp(i, color):
            if i == n - 1:
                return costs[i][color]

            total_cost = costs[i][color]
            if (i, color) not in memo:
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

