class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 1. intuition
        # flood fill from image[sr][sc]
        # directly adjacent(up, down, left, right) - same color
        if image[sr][sc] == color:
            return image

        n, m = len(image), len(image[0])
        original_color = image[sr][sc]

        def is_within_bounds(r, c):
            return 0 <= r < n and 0 <= c < m 

        def dfs(r: int, c: int):
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
            if not is_within_bounds(r, c):
                return
            if image[r][c] != original_color:
                return
            
            image[r][c] = color

            for d in dir:
                next_r, next_c = r + d[0], c + d[1]
                dfs(next_r, next_c)
        
        dfs(sr, sc)
        return image


        
