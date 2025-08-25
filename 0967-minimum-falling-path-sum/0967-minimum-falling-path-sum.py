class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dp(i, j):
            if j < 0 or j >= n:
                return float(inf)

            if i == m - 1:
                return matrix[i][j]

            if (i,j) not in memo:
                min_val = min(dp(i+1, j-1), dp(i+1, j), dp(i+1, j+1))
                memo[(i,j)] = min_val + matrix[i][j]

            return memo[(i,j)]
        
        memo = {}
        m,n = len(matrix), len(matrix[0])
        res = float(inf)
        for col in range(n):
            res = min(res, dp(0, col))
        return res
