class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # bottom up
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = int(obstacleGrid[0][0] != 1)
        for col in range(1, n):
            dp[0][col] = int(obstacleGrid[0][col] != 1 and dp[0][col-1] != 0)

        for row in range(1, m):
            dp[row][0] = int(obstacleGrid[row][0] != 1 and dp[row-1][0] != 0)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        # top down
        def dp(i, j):
            if obstacleGrid[i][j] == 1:
                memo[(i,j)] = 0
                return 0
            
            if i == 0 and j == 0:
                return 1
            
            if i == 0 and j > 0:
                memo[(i,j)] = int(dp(i, j-1) != 0)
                return memo[(i,j)]
            
            if j == 0 and i > 0:
                memo[(i,j)] = int(dp(i-1, j) != 0)
                return memo[(i,j)]
                

            if (i,j) not in memo:
                memo[(i,j)] = dp(i-1, j) + dp(i, j-1)

            return memo[(i,j)]
        
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dp(m-1, n-1)