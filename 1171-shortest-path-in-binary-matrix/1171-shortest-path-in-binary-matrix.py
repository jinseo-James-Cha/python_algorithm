from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # clear path? or -1
        # clear path = start from 0,0 to n-1, n-1 -> top left to bottom right
        # BFS
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def get_neighbours(row, col):
            neighbours = []
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            for ny, nx in directions:
                next_row, next_col = row + ny, col + nx
                if is_within_bounds(next_row, next_col) and grid[next_row][next_col] == 0:
                    neighbours.append((next_row, next_col))
            
            return neighbours



        n = len(grid)
        if n == 1:
            return -1 if grid[0][0] == 1 else 1
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        level = 1
        queue = deque([(0,0)])
        grid[0][0] = 1 # distance
        while queue:
            row, col = queue.popleft() # 0 0 
            if row == n-1 and col == n-1:
                return grid[row][col]
            
            for next_row, next_col in get_neighbours(row, col):
                grid[next_row][next_col] = grid[row][col] + 1
                queue.append((next_row, next_col))
        return -1



            
            