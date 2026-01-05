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
          h o r s e
        r 1 2 2 3 4
        o 2 1 3 3 4  
        s
        """
        # i <= j always.
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



