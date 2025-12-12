class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # min, max for each row and col
        min_row = [float('inf')] * (n+1)
        max_row = [0] * (n+1)
        min_col = [float('inf')] * (n+1)
        max_col = [0] * (n+1)
        for x, y in buildings:
            min_row[y] = min(min_row[y], x)
            max_row[y] = max(max_row[y], x)

            min_col[x] = min(min_col[x], y)
            max_col[x] = max(max_col[x], y)
        
        # minrow [-, -, 1, -]
        # maxrow [-, -, 1, -]
        # mincol [-, 2, -, -]
        # maxcol [-, 2, -, -]
        
        res = 0
        for x, y in buildings:
            if min_row[y] < x < max_row[y] and min_col[x] < y < max_col[x]:
                res += 1
        return res





        # dfs - TLE
        def is_within_bounds(row, col):
            return 0 <= row < n and 0 <= col < n

        DIRS = [(1,0), (-1,0), (0, 1), (0, -1)]
        def dfs(row, col, dy, dx):
            if not is_within_bounds(row, col):
                return False
            
            if graph[row][col]:
                return True
            
            return dfs(row+dy, col+dx, dy, dx)

        graph = [[False] * n for _ in range(n)]
        for x, y in buildings:
            graph[x-1][y-1] = True
        
        res = 0
        for x, y in buildings:
            covered = 0
            for dy, dx in DIRS:
                covered += dfs(x+dy-1, y+dx-1, dy, dx)
            
            if covered == 4:
                res += 1
        return res