from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        a path from (0,0) to (n-1, n-1)
        a cell in a path has minimum mahattan distance == safeness factor
        so, a path has different safeness factor and need to keep the minimum.

        for example
        0 0 1
        0 0 0
        1 0 0

        safeness factor
        2 1 0
        1 2 1
        0 1 2

        2 -> 1 -> 2 -> 1 -> 2 => this path is 1
        # we need to choose the maximum safeness factor every time to keep the minimum high
        # dijstra algorithm with max heap
        -2 -1  0
        -1 -2 -1
         0 -1 -2
        
        get all thieves and bfs to assign safeness factor
        starting from (0,0) -> put all options and pop from heapq and return


        0 0 1
        0 0 0
        1 0 0

        -3 -2 -1
        -2 -3 -2
        -1 -2 -3
        """
        # edge case
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        queue = deque()
        dist = [[-1]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    dist[row][col] = 0

        # bfs for safeness factor update
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, rc in DIRS:
                next_r, next_c = curr_r + dr, curr_c + rc
                if is_within_bounds(next_r, next_c) and dist[next_r][next_c] == -1:
                    dist[next_r][next_c] = dist[curr_r][curr_c] + 1
                    queue.append((next_r, next_c))

        # dijkstra algorithm
        pq = [(-dist[0][0], 0, 0)] # -3 0 0
        visited = [[False] * n for _ in range(n)]
        while pq:
            curr_safeness, r, c = heapq.heappop(pq)
            if r == n-1 and c == n-1:
                return -curr_safeness
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            for dr, dc in DIRS:
                next_r, next_c = dr+r, dc+c
                if is_within_bounds(next_r, next_c) and not visited[next_r][next_c]:
                    heapq.heappush(pq, (-min(-curr_safeness, dist[next_r][next_c]), next_r, next_c))
        
        return -1
