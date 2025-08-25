class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top down
        def dp(i, j):
            if i == 0 and j == 0:
                memo[(i,j)] = grid[i][j]
                return memo[(i,j)]
            
            if i == 0 and j > 0:
                memo[(i, j)] = dp(i, j-1) + grid[i][j]
                return memo[(i, j)]
            
            if j == 0 and i > 0:
                memo[(i, j)] = dp(i-1, j) + grid[i][j]
                return memo[(i, j)]

            if (i,j) not in memo:
                min_path = min(dp(i-1,j), dp(i,j-1))
                memo[(i,j)] = min_path + grid[i][j]
            
            return memo[(i,j)]
        
        memo = {}
        m,n = len(grid), len(grid[0])
        return dp(m-1, n-1)









        # top left 0 0 -> bottom right m - 1 n -1
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        def is_within_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            if r == n - 1 and c == m - 1:
                return grid[r][c]

            if dp[r][c] != 0:
                return dp[r][c]
            
            min_sum = float(inf)
            dir = [(1,0), (0, 1)] # down and right
            for dy, dx in dir:
                next_r, next_c = r + dy, c + dx
                if is_within_bounds(next_r, next_c):
                    min_sum = min(min_sum, dfs(next_r, next_c))
        
            dp[r][c] = grid[r][c] + min_sum
            return dp[r][c]
        return dfs(0, 0)
