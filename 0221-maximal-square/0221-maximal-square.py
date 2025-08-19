class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # square = 1, 4, 9, 16

        # 00 01 02 03 04 05
        # 10 11 12 13 14 15
        # 20 21 22 23 24 25
        # 30 31 32 33 34 35

        # [i][j]   [i][j+1]
        # [i+1][j] [i+1][j+1]
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


        # [
        #     ["1","0","1","0","0"],
        #     ["1","0","1","1","1"],
        #     ["1","1","1","1","1"],
        #     ["1","0","0","1","0"]
        #     ]



        # [
        # [0, 0, 0, 0, 0, 0], 
        # [0, 1, 0, 1, 0, 0], 
        # [0, 1, 0, 1, 1, 1], 
        # [0, 1, 1, 1, 2, 2], 
        # [0, 1, 0, 0, 1, 0]
        # ]