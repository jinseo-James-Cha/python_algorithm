class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 empty
        # 1 fresh
        # 2 rotten
        # change fresh to rotton
        
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row,col,0))
        
        if fresh_oranges == 0:
            return 0
        
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        max_minute = 0
        rotten_oranges = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col, minute = queue.popleft()
                max_minute = max(max_minute, minute)
                for dy, dx in DIRS:
                    next_row, next_col = row+dy, col+dx
                    if (0 <= next_row < m and 0 <= next_col < n) and grid[next_row][next_col] == 1:
                        queue.append((next_row, next_col, minute+1))
                        grid[next_row][next_col] = 2
                        rotten_oranges += 1
        return max_minute if fresh_oranges == rotten_oranges else -1
