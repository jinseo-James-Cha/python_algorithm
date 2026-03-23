from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # binary search + bfs
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def is_valid_safeness(grid, minSafeness):
            n = len(grid)
            if grid[0][0] < minSafeness or grid[n-1][n-1] < minSafeness:
                return False
            
            queue = deque([(0,0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while queue:
                curr_r, curr_c = queue.popleft()
                if curr_r == n-1 and curr_c == n-1:
                    return True
                
                for dr, dc in DIRS:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    if is_within_bounds(next_r, next_c) and not visited[next_r][next_c] and grid[next_r][next_c] >= minSafeness:
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))

            return False

        
        # update 1 -> 0 and 0 -> -1
        n = len(grid)
        queue = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    grid[row][col] = 0
                else:
                    grid[row][col] = -1
        
        # bfs
        # update with safeness factor
        safeness = 1
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                for dr, dc in DIRS:
                    next_r, next_c = r+dr, c+dc
                    if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == -1:
                        grid[next_r][next_c] = safeness
                        queue.append((next_r, next_c))
            safeness += 1

        # binary search for possible answers 0~ max safeness
        left = 0
        right = safeness
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if is_valid_safeness(grid, mid):
                res = mid
                left = mid + 1
            else:
                right = mid -1
        return res
        






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
        pq = [(-dist[0][0], 0, 0)]
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
