class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Q?
        - can I change values in the grid?
        - only "1" or "0"?

        find a "1" and dfs and check visited -> if it is done count += 1
        I can put label starting from "2" and return label - 2
        """
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, label):
            grid[row][col] = str(label)

            for dr, dc in DIRS:
                next_r, next_c = row+dr, col+dc
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == "1":
                    dfs(next_r, next_c, label)

        label = 2
        m,n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    dfs(row, col, label)
                    label += 1
        
        return label - 2
