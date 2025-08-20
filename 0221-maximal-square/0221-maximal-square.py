class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # square = 1, 4, 9, 16

        # 00 01 02 03 04 05
        # 10 11 12 13 14 15
        # 20 21 22 23 24 25
        # 30 31 32 33 34 35

        # [i][j]   [i][j+1]
        # [i+1][j] [i+1][j+1]
        
        # bottom up
        max_square = 0
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        dp = [[0] * (cols) for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                    max_square = max(max_square, dp[r][c])

        return max_square * max_square
        






        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        maxsqlen = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen


        # top down
        # def dp(i, j):
        #     if i == 0 or j == 0:
        #         return 0
            
        #     if (i,j) not in memo:
        #         if matrix[i-1][j-1] == "1":
        #             memo[(i,j)] = min(dp(i-1, j-1), dp(i-1, j), dp(i, j-1)) + 1
        #         else:
        #             memo[(i,j)] = 0
            
        #     return memo[(i,j)]
        
        # memo = {}
        # rows = len(matrix) + 1
        # cols = len(matrix[0]) + 1
        # largest_square = 0
        # for r in range(1, rows):
        #     for c in range(1, cols):
        #             largest_square = max(largest_square, dp(r, c))
        # return largest_square * largest_square