class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        abcde , ace
        - - -   --- => return 3
        find how many characters are matched in the order
        """

        """
        DP top down
           a b c
        a  1 1 1
        c  1 1 2

           a b c d e
        a  1 1 1 1 1
        c  1 1 2 2 2
        e  1 1 2 2 3
        if the same characters => prev,prev + 1
        if not, max(prev up, prev left) 
        """
        def dp(t1_idx, t2_idx):
            if t1_idx < 0 or t2_idx < 0:
                return 0
            
            if (t1_idx, t2_idx) not in memo:
                curr = 0
                if text1[t1_idx] == text2[t2_idx]:
                    curr = dp(t1_idx-1, t2_idx-1) + 1
                else:
                    curr = max(dp(t1_idx, t2_idx-1), dp(t1_idx-1, t2_idx))
                memo[(t1_idx, t2_idx)] = curr
            return memo[(t1_idx, t2_idx)]

        memo = {}
        return dp(len(text1)-1, len(text2)-1)


        """
        brute force solution
        find all subsequence from the both
        abc => "", "a", "b", "c", "ab", "ac", "bc", "abc" => 2^len("abc")
        ac => "", "a", "c", "ac" => 2^len("ac)
        
        time complexity = O(n · 2^n + m · 2^m))

        """
        if text1 == text2:
            return len(text1)

        def backtrack(text, curr, start, result):            
            result.append("".join(curr[:]))
            
            for i in range(start, len(text)):
                curr.append(text[i])
                backtrack(text, curr, i+1, result)
                curr.pop()

        text1_subsequences = []
        text2_subsequences = []
        
        backtrack(text1, [], 0, text1_subsequences)
        backtrack(text2, [], 0, text2_subsequences)
        text2_subsequences = set(text2_subsequences)

        max_len = 0
        for t1_sub in text1_subsequences:
            if t1_sub in text2_subsequences:
                max_len = max(max_len, len(t1_sub))
        return max_len
        





















        # dp - bottom up
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