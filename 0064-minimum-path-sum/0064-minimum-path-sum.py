import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # index start row0, col0 -> end m-1, n-1
        # shortest path with weight -> Dijkstra bfs
        # only move down or right
        # 1 3 1
        # 1 5 1
        # 4 2 1
        
        # dijkstra algorithm - weighted shortest path
        m, n = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)] # sum, row, col
        visited = set((0,0)) # started
        DIRS = [(1,0), (0,1)]

        while q:
            curr_sum, row, col = heapq.heappop(q)
            if row == m-1 and col == n-1:
                return curr_sum
            
            for dy, dx in DIRS:
                next_r, next_c = row+dy, col+dx
                if next_r < m and next_c < n and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    heapq.heappush(q, (curr_sum + grid[next_r][next_c], next_r, next_c))
        return -1

        
        
        
        
        
        # dp - bottom up
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # base case
        row_sum = 0
        for row in range(m):
            row_sum += grid[row][0]
            dp[row][0] = row_sum
        
        col_sum = 0
        for col in range(n):
            col_sum += grid[0][col]
            dp[0][col] = col_sum
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[m-1][n-1]


        # dp - top down
        m, n = len(grid), len(grid[0])
        def dp(row, col): # 3, 3 -> min(dp(2, 3), dp(3, 2)) + grid[3][3]
            if row == 0 and col == 0:
                return grid[row][col]
           
            if (row,col) not in memo:
                minimum = 0
                if row == 0:
                    minimum = dp(row, col-1) + grid[row][col]
                elif col == 0:
                    minimum = dp(row-1, col) + grid[row][col]
                else:
                    minimum = min(dp(row-1, col), dp(row, col-1)) + grid[row][col]
                memo[(row, col)] = minimum
            return memo[(row, col)]
        memo = {}
        return dp(m-1, n-1)












        # bottom up
        m,n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]
        for col in range(1, n):
            dp[0][col] = grid[0][col] + dp[0][col-1]
        
        for row in range(1, m):
            dp[row][0] = grid[row][0] + dp[row-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
        

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
