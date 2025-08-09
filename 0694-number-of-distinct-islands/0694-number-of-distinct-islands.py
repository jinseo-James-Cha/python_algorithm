class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # the main point : how can I have distinct ...?
        # using set to save the shape?
        # r c - new r c
        n, m = len(grid), len(grid[0])

        def is_within_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(r, c, start_r, start_c, shape):
            grid[r][c] = -1

            for dy, dx in DIR:
                next_r, next_c = r + dy, c + dx
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                    shape.append((next_r - start_r, next_c - start_c))
                    dfs(next_r, next_c, start_r, start_c, shape)
            
        res = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    shape = [(0,0)]
                    dfs(r, c, r, c, shape)
                    res.add(tuple(shape))
        return len(res)
