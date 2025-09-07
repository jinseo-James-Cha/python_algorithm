class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, up, down = len(grid[0]), 0, len(grid), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    left = min(left, j)
                    right = max(right, j)

                    up = min(up, i)
                    down = max(down, i)
        
        return (right - left + 1) * (down - up + 1)