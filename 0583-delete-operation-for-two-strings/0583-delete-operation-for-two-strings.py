class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        memo = {}

        def lcs(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i,j)]
            
            if word1[i] == word2[j]:
                memo[(i,j)] = 1 + lcs(i+1, j+1)
            else:
                memo[(i,j)] = max(lcs(i+1, j), lcs(i, j+1))
            
            return memo[(i,j)]
            
        lcs_len = lcs(0,0)
        return m + n - 2 * lcs_len
