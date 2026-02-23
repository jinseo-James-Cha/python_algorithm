class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # '1' => land or '0' => water
        # return number of islands
        
        # count 1 and mark its connected cells -> 1 island
        # out of bounds => water

        # can I color(change) the value in grid? -> YES
        # put island id and then dfs to color all land cells with id
        # id starts from 2 and return id - 1

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        DIRS = [(1,0), (-1,0), (0,-1), (0,1)]
        def dfs(row, col, island_id):
            grid[row][col] = str(island_id)

            for dr, dc, in DIRS:
                next_row, next_col = row + dr, col + dc
                if is_within_bounds(next_row, next_col) and grid[next_row][next_col] == '1':
                    dfs(next_row, next_col, island_id)

        island_id = 2
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col, island_id)
                    island_id += 1

        return island_id - 2

















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
        



