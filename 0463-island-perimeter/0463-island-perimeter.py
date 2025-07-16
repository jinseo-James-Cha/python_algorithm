class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def is_within_bounds(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c):
            nonlocal perimeter
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up down left right
            for d in dir:
                next_r, next_c = r + d[0], c + d[1]
                if not is_within_bounds(next_r, next_c):
                    perimeter += 1
                elif grid[next_r][next_c] == 0:
                    perimeter += 1

                if (
                    is_within_bounds(next_r, next_c) 
                    and visited[next_r][next_c] == False
                    and grid[next_r][next_c] == 1
                    ):
                    visited[next_r][next_c] = True
                    dfs(next_r, next_c)

        # 1 = land, 0 = water
        perimeter = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and visited[r][c] == False:
                    visited[r][c] = True
                    dfs(r,c)
        return perimeter