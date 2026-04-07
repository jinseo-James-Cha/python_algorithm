from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # can destroy k obstacles
        # direction 4 and k > 0

        m,n = len(grid), len(grid[0])
        visited = set()

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque([(0,0,k,0)])
        while queue:
            curr_row, curr_col, curr_k, curr_step = queue.popleft()
            if curr_row == m-1 and curr_col == n-1:
                return curr_step

            for dr, dc in DIRS:
                nr, nc = curr_row + dr, curr_col + dc
                if is_within_bounds(nr, nc):
                    nk = curr_k - grid[nr][nc]
                    if nk >= 0 and (nr, nc, nk) not in visited:
                        visited.add((nr, nc, nk))
                        queue.append((nr, nc, nk, curr_step + 1))
        return -1


