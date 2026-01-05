class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m, n grid
        start = [0, 0]
        end = [m-1, n-1]
        move = Down or Right

        for example
        3 * 6
        
        S00 01 02 03 04 05
         10 11 12 13 14 15
         20 21 22 23 24 E25

        1 1 1 1 1 1
        1 2 3 4 5 6
        1 3 6 10 15 21

        => dp m, n -> m-1,n + m, n-1
        """
        # bottom up
        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]


        # top down
        def dp(row, col):
            if row == 0 or col == 0:
                return 1
            
            if (row, col) not in memo:
                memo[(row, col)] = dp(row-1, col) + dp(row, col-1)
            
            return memo[(row, col)]
        
        memo = {}
        return dp(m-1, n-1)