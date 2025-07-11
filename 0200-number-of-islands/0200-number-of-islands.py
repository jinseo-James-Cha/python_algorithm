class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. intuition
        # using nested for loop to get count of islands
        # if found and not visited, send DFS
        # using DFS to search connected if it is not visited
        # return count

        # 2. complexity
        # DFS : O(V+E)
        # V = m * n
        # E = 4V  # can connect up down left right
        # but it is Undirected graph
        # E == 2V == 2 m * n
        # O(3m*n) -> O(m * n) -> 300 * 300 => 90000

        # 3. data structure
        # grid: List[List[str]]
        # visited List[List[bool]]
        # res: int
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and visited[r][c] == False:
                    visited[r][c] = True
                    res += 1
                    self.dfs(r, c, grid, visited)
        
        return res
    def dfs(self, r: int, c: int, grid: List[List[str]], visited: List[List[bool]]) -> None:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        for d in dir:
            next_r, next_c = r + d[0], c + d[1]
            if self.is_within_bounds(next_r,next_c, grid) and grid[next_r][next_c] == "1" and visited[next_r][next_c] == False:
                visited[next_r][next_c] = True
                self.dfs(next_r, next_c, grid, visited)
        
    def is_within_bounds(self, r: int, c: int, grid: List[List[str]]) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])



# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # up, down, left, right
#         # dy(1, -1, 0, 0)
#         # dx(0, 0, -1, 1)
#         # direction vertors: dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]       
#         if not grid:
#             return 0
#         count = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "1":
#                     self.dfs(r, c, grid)
#                     count += 1
#         return count
#     # DFS
#     def dfs(self, r: int, c: int, grid: List[List[str]]) -> None:
#         # mark current land cell as visited with -1
#         grid[r][c] = "-1"

#         # up, down, left, right
#         # row, column order cuz of 2D matrix
#         dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]

#         for d in dirs:
#             next_r, next_c = r + d[0], c + d[1]
#             if (self.is_within_bounds(next_r, next_c, grid) and grid[next_r][next_c] == "1"):
#                 self.dfs(next_r, next_c, grid)

#     def is_within_bounds(self, r: int, c: int, grid: List[List[str]]) -> bool:
#             return 0 <= r < len(grid) and 0 <= c < len(grid[0])