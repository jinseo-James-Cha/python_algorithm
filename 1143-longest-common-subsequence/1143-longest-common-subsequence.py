class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp
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