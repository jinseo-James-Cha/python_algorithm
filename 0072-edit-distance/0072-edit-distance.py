class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = bottom up

        # base case
        word1_len = len(word1)
        word2_len = len(word2)
        if word1_len == 0:
            return word2_len
        if word2_len == 0:
            return word1_len

        # initial data
        dp = [[0] * (word2_len+1) for _ in range(word1_len+1)]
        for i in range(word1_len+1):
            dp[i][0] = i
        for j in range(word2_len+1):
            dp[0][j] = j

        # dp
        for i in range(1, word1_len+1):
            for j in range(1, word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
        return dp[word1_len][word2_len]






        # dp - top down
        def dp(word1_idx, word2_idx):
            if word1_idx == 0:
                return word2_idx
            if word2_idx == 0:
                return word1_idx
            
            if (word1_idx, word2_idx) not in memo:
                # matched
                min_distance = 0
                if word1[word1_idx-1] == word2[word2_idx-1]:
                    min_distance = dp(word1_idx-1, word2_idx-1)
                else:
                    # insert
                    insert_distance = dp(word1_idx, word2_idx-1)
                    # delete
                    delete_distance = dp(word1_idx-1, word2_idx)
                    # replace
                    replace_distance = dp(word1_idx-1, word2_idx-1)

                    min_distance = min(insert_distance, delete_distance, replace_distance) + 1

                memo[(word1_idx, word2_idx)] = min_distance

            return memo[(word1_idx, word2_idx)]
        memo = {}
        return dp(len(word1), len(word2))













        # bottom up
        


        # minimum number of operations word1 -> word2
        # top down
        memo = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def calculate_distance_in_memo(word1, word2, word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if memo[word1Index][word2Index] is not None:
                return memo[word1Index][word2Index]

            if word1[word1Index-1] == word2[word2Index-1]:
                minEditDistance = calculate_distance_in_memo(word1, word2, word1Index-1, word2Index-1)
            else:
                insertOperation = calculate_distance_in_memo(word1, word2, word1Index, word2Index - 1)
                deleteOperation = calculate_distance_in_memo(
                    word1, word2, word1Index - 1, word2Index
                )
                replaceOperation = calculate_distance_in_memo(
                    word1, word2, word1Index - 1, word2Index - 1
                )
                minEditDistance = (
                    min(insertOperation, deleteOperation, replaceOperation) + 1
                )
            memo[word1Index][word2Index] = minEditDistance
            return minEditDistance

        return calculate_distance_in_memo(word1, word2, len(word1), len(word2))