from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 empty
        # 1 fresh
        # 2 rotton
        m,n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)] 

        # save fresh oranges
        freshes = set()
        rottons = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshes.add((i,j))
                elif grid[i][j] == 2:
                    rottons.append((i,j))
        
        # bfs
        res = 0
        queue = deque(rottons)
        while queue:
            removed = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    next_r, next_c = r+dr, c+dc
                    if 0 <= next_r < m and 0 <= next_c < n and (next_r, next_c) in freshes:
                        queue.append((next_r, next_c))
                        freshes.remove((next_r, next_c))
                        removed = True
            if removed:
                res += 1
        return res if len(freshes) == 0 else -1










        queue = deque() #
        num_of_fresh = 0 #
        n, m = len(grid), len(grid[0]) #
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    num_of_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        if num_of_fresh == 0:
            return 0
        
        def is_within_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        minutes = 0
        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        # bfs
        while queue and num_of_fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dy, dx in DIR:
                    next_r, next_c = r + dy, c + dx
                    if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        num_of_fresh -= 1
                        queue.append((next_r, next_c))
            minutes += 1

        return -1 if num_of_fresh > num_of_rotten else res
