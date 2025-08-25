class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # state
        # i for rows
        # j for cols

        # bottom up
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


        # top down
        def dp(i, j):
            if i == 0 or j == 0:
                return 1
            
            if (i,j) not in memo:
                memo[(i,j)] = dp(i-1, j) + dp(i, j-1)

            return memo[(i,j)]
        
        memo = {}
        return dp(m-1, n-1)










        # grid[m - 1][n - 1] = grid[m-2][n-1] + grid[m-1][n-2]

        # bottom up
        dp = [[1 for _ in range(n)] for _ in range(m)] 
        for r in range(1, m): 
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
