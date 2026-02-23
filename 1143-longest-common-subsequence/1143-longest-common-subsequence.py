class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp- bottom up
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]






        # LCS
        # naive 
        #   a b c d e
        # a 1 1 1 1 1
        # c 1 1 2 2 2
        # e 1 1 2 2 3
        # text1[i] == text2[j]: dp[i-1][j-1] + 1
        # text1[i] != text2[j]: max(dp[i-1][j], dp[i][j-1])
        def dp(i, j):
            if i == 0 or j == 0:
                return 0

            if (i, j) not in memo:
                if text1[i-1] == text2[j-1]:
                    memo[(i,j)] = dp(i-1, j-1) + 1
                else:
                    memo[(i,j)] = max(dp(i-1, j), dp(i, j-1))
            
            return memo[(i,j)]
            
        memo = {}
        return dp(len(text1), len(text2))

        # dp bottom up
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

        
        
        # dp top down
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) not in memo:
                if text1[i] == text2[j]:
                    memo[(i, j)] = dp(i+1, j+1) + 1
                else:
                    memo[(i, j)] = max(dp(i+1, j), dp(i, j+1))
            return memo[(i,j)]
        memo = {}
        return dp(0, 0)
        
        
        # dp backward
        m, n = len(text1), len(text2)

        def dp(text1_idx, text2_idx):
            if text1_idx < 0 or text2_idx < 0:
                return 0

            if (text1_idx, text2_idx) not in memo:
                if text1[text1_idx] == text2[text2_idx]:
                    memo[(text1_idx, text2_idx)] = dp(text1_idx-1, text2_idx-1) + 1
                else:
                    memo[(text1_idx, text2_idx)] =  max(dp(text1_idx-1, text2_idx), dp(text1_idx, text2_idx-1))
            return memo[(text1_idx, text2_idx)]

        memo = {}
        return dp(m-1, n-1)