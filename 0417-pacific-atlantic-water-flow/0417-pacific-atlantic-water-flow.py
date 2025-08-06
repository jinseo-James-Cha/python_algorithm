class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # problem
        # heights -> height above sea level
        # a cell can move to less than or equal to the neighbors
        # if the cell can move upto the oceans, it needed to save in res


        # pacific_ocean - top left
        # atlantic_ocean - bottom right
        # row 0    col 0 -> pacific
        # row n-1  col n-1 -> atlantic

        def is_within_bounds(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])

        DIR = [(-1,0), (0,-1), (1,0), (0,1)] # up left down right
        def dfs(r, c, visited):
            visited.add((r, c))
            
            for dy, dx in DIR:
                next_r, next_c = r + dy, c + dx
                if is_within_bounds(next_r, next_c) and (next_r, next_c) not in visited and heights[next_r][next_c] >= heights[r][c]:
                    dfs(next_r, next_c, visited)

        # 반대로 생각해서 바다에서 갈수있는 셀을 다 각각저장하자
        pacific_reachable = set()
        atlantic_reachable = set()
        n = len(heights)
        m = len(heights[0])

        for r in range(n):
            dfs(r, 0, pacific_reachable) 
            dfs(r, m-1, atlantic_reachable) 
        
        for c in range(m):
            dfs(0, c, pacific_reachable)
            dfs(n-1, c, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)