class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
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