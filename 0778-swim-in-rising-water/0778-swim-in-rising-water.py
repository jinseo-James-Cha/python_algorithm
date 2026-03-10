import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [(1,0), (-1,0), (0,-1), (0,1)]
        visited = set((0,0))
        pq = [(grid[0][0], 0, 0)] # (depth, row, col)

        res = 0

        def is_within_bounds(row, col):
            return 0 <= row < n and 0 <= col < n

        while pq:
            curr_depth, row, col = heapq.heappop(pq)
            res = max(res, curr_depth)
            if row == n-1 and col == n-1:
                break
            
            for dr, dc in DIRS:
                next_r, next_c = row + dr, col + dc
                if is_within_bounds(next_r, next_c) and (next_r,next_c) not in visited:
                    heapq.heappush(pq, (grid[next_r][next_c], next_r, next_c))
                    visited.add((next_r, next_c))

        return res
            

