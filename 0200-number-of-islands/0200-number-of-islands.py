class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # char '1' or '0' -> '0' if visited
        m, n = len(grid), len(grid[0])
        res = 0
        DIRS = [(-1,0), (1,0), (0,1), (0,-1)] # up down right left

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            grid[row][col] = '0' # visited

            for dy, dx in DIRS:
                next_r, next_c = dy+row, dx+col
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == '1':
                    dfs(next_r, next_c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
        



