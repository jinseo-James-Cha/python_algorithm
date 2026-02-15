class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Strictly greater than 4directions

        # dfs
        m, n = len(mat), len(mat[0])

        def is_within_bound(row,col):
            if row < 0 or row >= len(mat):
                return False
            
            if col < 0 or col >= len(mat[0]):
                return False
            
            return True

        def dfs(row, col, val):
            if not is_within_bound(row, col):
                return 1
            
            return int(mat[row][col] < val)


        for row in range(m):
            for col in range(n):
                up = dfs(row-1, col, mat[row][col])
                down = dfs(row+1, col, mat[row][col])
                left = dfs(row, col-1, mat[row][col])
                right = dfs(row, col+1, mat[row][col])
                if up+down+left+right == 4:
                    return [row, col]

        return [-1, -1]