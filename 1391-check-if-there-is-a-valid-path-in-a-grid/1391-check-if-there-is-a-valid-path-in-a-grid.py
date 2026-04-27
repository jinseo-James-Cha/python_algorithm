from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        BFS

        1 -> 3,4,5,6
        2 -> 3,4,5,6
        3 -> 1,2,4,5,6
        4 -> 1,2,3,5,6
        5 -> 1,2,3,4,6
        6 -> 1,2,3,4,5

        """
        DIRS = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }
        def is_within_bound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True

        queue = deque([(0, 0)])
        while queue:
            curr_row, curr_col = queue.popleft()
            if curr_row == m - 1 and curr_col == n - 1:
                return True

            for dr, dc in DIRS[grid[curr_row][curr_col]]:
                next_row, next_col = curr_row + dr, curr_col + dc
                if is_within_bound(next_row, next_col) and not visited[next_row][next_col]:
                    
                    for bdr, bdc in DIRS[grid[next_row][next_col]]:
                        if next_row + bdr == curr_row and next_col + bdc == curr_col:
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
        return False

