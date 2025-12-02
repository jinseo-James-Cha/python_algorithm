class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
          a b c d e
        a 1 1 1 1 1
        c 1 1 2 2 2
        e 1 1 2 2 3

          b s b i n i n m
        j 0 0 0 0 0 0 0 0
        m 0 0 0 0 0 0 0 1
        j 0 0 0 0 0 0 0 1
        k 0 0 0 0 0 0 0 1
        b 1 1 1 1 1 1 1 1 - > this is the problem b has 2 so it is 2
        k 1 1 1 1 1 1 1 1
        j 1 1 1 1 1 1 1 1
        k 1 1 1 1 1 1 1 1
        v 1 1 1 1 1 1 1 1

        """ 
        # dp bottom up
        text1_len, text2_len = len(text1), len(text2)
        dp = [[0] * (text1_len+1) for _ in range(text2_len+1)]
        
        # backward
        for row in range(text2_len - 1, -1, -1):
            for col in range(text1_len -1 , -1, -1):
                if text1[col] == text2[row]:
                    dp[row][col] = dp[row+1][col+1] + 1
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]




        # dp top down
        def dp(text1_idx, text2_idx):
            # base case
            if text1_idx < 0 or text2_idx < 0:
                return 0
            
            if (text1_idx, text2_idx) not in memo:
                lcs = 0
                if text1[text1_idx] == text2[text2_idx]:
                    lcs = dp(text1_idx-1, text2_idx-1) + 1
                else:
                    lcs = max(dp(text1_idx-1, text2_idx), dp(text1_idx, text2_idx-1))
                memo[(text1_idx, text2_idx)] =  lcs
            return memo[(text1_idx, text2_idx)]
        
        memo = {}
        m, n = len(text1), len(text2)
        return dp(m-1, n-1)








        # backward
        # dp[text1index][text2index]

        # bottom up
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        # backward
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]




        # top down
        # def dp(t1_i, t2_i):
        #     if t1_i == t1 or t2_i == t2:
        #         return 0
            
        #     if (t1_i, t2_i) not in memo:
        #         if text1[t1_i] == text2[t2_i]:
        #             memo[(t1_i, t2_i)] = 1 + dp(t1_i + 1, t2_i + 1)
        #         else:
        #             memo[(t1_i, t2_i)] = max(dp(t1_i + 1, t2_i), dp(t1_i, t2_i + 1))
                
        #     return memo[(t1_i, t2_i)]
        
        # t1, t2 = len(text1), len(text2)
        # memo = {}
        # return dp(0,0)














       
       
       
       
       
       
       
       
       
       
        # dp = [0] * len(text1)
        # longest_length = 0

        # for t2 in text2:
        #     current_num = 0
        #     for i, length in enumerate(dp):
        #         if length > current_num:
        #             current_num = length
        #         elif text1[i] == t2:
        #             dp[i] = current_num + 1
        #             longest_length = max(longest_length, dp[i])
        
        # return longest_length

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