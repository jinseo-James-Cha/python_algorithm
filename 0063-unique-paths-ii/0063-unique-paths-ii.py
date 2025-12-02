class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # unique path
        # can I modify the grid?
        # only 1, 0?
        # dp top down
        # two ways from left or above
        # current = left possibility + above possibility
        # 0 0 0 -> 1 1 1
        # 0 1 0 -> 1 0 1
        # 0 0 0 -> 1 1 2

        # 1 0 -> 0 0
        def dp(row, col): # 2 2 -> dp(1, 2) + dp(2, 1) -> dp(0, 2) + dp(1, 1)=0 -> dp
            # base case -> obstacle? return 0
            # base case -> always 1 for row 0 or col 0

            # out of bound
            if row < 0 or col < 0:
                return 0

            # base case 
            if obstacleGrid[row][col] == 1:
                return 0
            
            if row == 0 and col == 0:
                return 1
            
            if (row, col) not in memo:
                path = 0
                if row == 0:
                    path = dp(row, col-1)
                elif col == 0:
                    path = dp(row-1, col)
                else:
                    path = dp(row-1, col) + dp(row, col-1)
                memo[(row, col)] = path
            return memo[(row, col)]
            
        memo = {}
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        return dp(m-1, n-1)











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