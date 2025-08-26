class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # bottom up
        n = len(costs) # houses
        k = len(costs[0]) # colors
        dp = [[0] * k for _ in range(n)]

        # base case
        for j in range(k):
            dp[0][j] = costs[0][j]
        
        for i in range(1, n):
            for j in range(k):
                min_cost = float(inf)
                for z in range(k):
                    if j != z:
                        min_cost = min(min_cost, dp[i-1][z])
                dp[i][j] = min_cost + costs[i][j]
        
        return min(dp[n-1])





        # top down
        def dp(row, col):
            if row == n-1:
                return costs[row][col]

            if (row,col) not in memo:
                min_cost = float(inf)
                for c in range(k):
                    if c != col:
                        min_cost = min(min_cost, dp(row+1, c))
                memo[(row, col)] = min_cost + costs[row][col]
            return memo[(row, col)]
        
        n = len(costs) # houses
        k = len(costs[0]) # colors
        memo = {}
        res_min = float(inf)
        for i in range(k):
            res_min = min(res_min, dp(0,i))
        
        return res_min