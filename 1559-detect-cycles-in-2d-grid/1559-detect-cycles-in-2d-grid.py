class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        dfs
        """
        def is_within_bound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(curr_row, curr_col, prev_row, prev_col, check_val):
            if (curr_row, curr_col) in visited:
                return True
            
            visited.add((curr_row, curr_col))
            for dr, dc in DIRS:
                next_row, next_col = curr_row + dr, curr_col + dc
                if is_within_bound(next_row, next_col):
                    if grid[next_row][next_col] == check_val:
                        if (next_row, next_col) == (prev_row, prev_col):
                            continue
                        
                        if dfs(next_row, next_col, curr_row, curr_col, check_val):
                            return True
            return False

        m, n = len(grid), len(grid[0])
        visited = set()
        for row in range(m):
            for col in range(n):
                if (row, col) not in visited:
                    if dfs(row, col, -1, -1, grid[row][col]):
                        return True
        return False