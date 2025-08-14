
# it's hard for me..
# need to solve a few more times
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest_length = 0

        for t2 in text2:
            current_num = 0
            for i, length in enumerate(dp):
                if length > current_num:
                    current_num = length
                elif text1[i] == t2:
                    dp[i] = current_num + 1
                    longest_length = max(longest_length, dp[i])
        
        return longest_length











        # DP - ninja
        # dp = [0] * len(text1) # 0 0 0 0
        # longest_length = 0

        # for t2 in text2:
        #     current_length = 0
        #     for i, length in enumerate(dp):
        #         if length > current_length:
        #             current_length = length
        #         elif t2 == text1[i]:
        #             dp[i] = current_length + 1
        #             longest_length = max(longest_length, current_length + 1)
        # return longest_length



        # DP
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]