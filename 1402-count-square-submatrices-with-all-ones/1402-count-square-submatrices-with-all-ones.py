class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # 0 1 1 1 -> 3
        # 1 1 2 2 -> 6
        # 0 1 2 3 -> 6

        # 0 0 0 0 0
        # 0 0 1 1 1
        # 0 1 1 2 2
        # 0 0 1 2 3

        res = 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]

        for row in range(1, m+1):
            for col in range(1, n+1):
                if matrix[row-1][col-1] == 1:
                    dp[row][col] = 1 + min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])
                    res += dp[row][col]

        return res
