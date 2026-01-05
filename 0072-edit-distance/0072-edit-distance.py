class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Convert word1 to work2
        Return minimum operations.

        operation
        1. Insert a character
        2. Delete a character
        3. Replace a character

        state: indices of word1 and word2 and operation..
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    do_deleting = dp[i-1][j]
                    do_inserting = dp[i][j-1]
                    do_replacing = dp[i-1][j-1]
                    dp[i][j] = min(do_deleting, do_inserting, do_replacing) + 1
        return dp[m][n]


        def dp(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            
            if (i, j) not in memo:
                # do_nothing
                if word1[i-1] == word2[j-1]:
                    memo[(i, j)] = dp(i-1, j-1)
                else:
                    do_inserting = dp(i, j-1)
                    do_deleting = dp(i-1, j)
                    do_replacing = dp(i-1, j-1)
                    memo[(i, j)] = min(do_inserting, do_deleting, do_replacing) + 1
            return memo[(i, j)]

        memo = {}
        return dp(len(word1), len(word2))



