class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
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