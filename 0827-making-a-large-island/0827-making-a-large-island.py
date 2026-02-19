class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # coloring !
        n = len(grid)
        
        # 0,1은 사용중이라 2부터 시작
        island_id = 2
        area = {}
        
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            
            grid[r][c] = island_id
            size = 1
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                size += dfs(r+dr, c+dc)
            
            return size
        
        # 1️⃣ 각 섬 라벨링
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r, c)
                    island_id += 1
        
        res = 0
        for size in area.values():
            res = max(res, size)
        
        # 2️⃣ 0을 1로 바꿔보기
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1
                    
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n:
                            id_ = grid[nr][nc]
                            if id_ > 1 and id_ not in seen:
                                new_size += area[id_]
                                seen.add(id_)
                    
                    res = max(res, new_size)
        
        return res



        """
        10
        01

        wildcard used or not
        if not used, I can change to 1 and wildcard used and keep checking other cells
        if used and 0, stop the loop

        dfs(row, col)
        """
        # def is_within_bounds(row, col):
        #     return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        # DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        # def dfs(row, col, wildcard, visited):
        #     visited.add((row, col))

        #     curr = 0
        #     if grid[row][col] == 1:
        #         curr = 1
        #     elif wildcard:
        #         curr = 1
        #         wildcard = False

        #     for dy, dx in DIRS:
        #         next_row, next_col = row+dy, col+dx
        #         if is_within_bounds(next_row, next_col) and (next_row, next_col) not in visited:
        #             if grid[next_row][next_col]:
        #                 curr += dfs(next_row, next_col, wildcard, visited)
        #             elif wildcard:
        #                 curr += dfs(next_row, next_col, wildcard, visited)
            
        #     return curr

        # n = len(grid)
        # res = 0
        # for row in range(n):
        #     for col in range(n):
        #         if grid[row][col]:
        #             total_size = dfs(row, col, True, set())
        #             res = max(res, total_size)
        # return res