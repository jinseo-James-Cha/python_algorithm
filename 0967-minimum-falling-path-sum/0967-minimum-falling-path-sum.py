class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # bottom up
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            dp[m-1][col] = matrix[m-1][col]
        
        for i in range(m-2, -1, -1):
            for j in range(n):
                down = dp[i+1][j]
                left = dp[i+1][j-1] if j-1 >= 0 else float("inf")
                right = dp[i+1][j+1] if j+1 < n else float("inf")

                dp[i][j] = min(down, left, right) + matrix[i][j]

        return min(dp[0])









        # top down
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
