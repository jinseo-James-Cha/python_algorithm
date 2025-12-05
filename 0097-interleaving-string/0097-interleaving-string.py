class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp - bottom up
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1)+1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0 :
                    dp[i][j] = True
                
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                
                else:
                    s1_match = dp[i-1][j] and s1[i-1] == s3[i + j - 1]
                    s2_match = dp[i][j-1] and s2[j-1] == s3[i + j - 1]
                    dp[i][j] = s1_match or s2_match
        return dp[len(s1)][len(s2)]
                




        
        # dp - top down
        # add index when they matching?
        # if len(s3) != len(s1) + len(s2):
        #     return False

        # def dp(s1_idx, s2_idx, s3_idx):
        #     if s3_idx == len(s3):
        #         return True
            
        #     if (s1_idx, s2_idx, s3_idx) not in memo:
        #         possible = False
        #         if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
        #             possible = dp(s1_idx+1, s2_idx, s3_idx+1)
                
        #         if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
        #             possible = possible or dp(s1_idx, s2_idx+1, s3_idx+1)
                
        #         memo[(s1_idx, s2_idx, s3_idx)] = possible
            
        #     return memo[(s1_idx, s2_idx, s3_idx)]
            
        # memo = {}
        # return dp(0, 0, 0)

        # # s3 formed by interleaving s1 and s2
        
        # # state
        # # index of s3
        # if len(s3) != len(s1) + len(s2):
        #     return False
        # dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # for i in range(len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i == 0 and j == 0:
        #             dp[i][j] = True
        #         elif i == 0:
        #             dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        #         elif j == 0:
        #             dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
        #         else:
        #             dp[i][j] = (
        #                 dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
        #             ) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        # return dp[len(s1)][len(s2)]

        # # Top down
        # @cache
        # def dp(i, i_s1, i_s2):
        #     if i != len(s3) and i_s1 == len(s1) and i_s2 == len(s2):
        #         return False
                
        #     if i == len(s3):
        #         if i_s1 == len(s1) and i_s2 == len(s2):
        #             return True
        #         else: 
        #             return False
            
        #     if i_s1 == len(s1):
        #         return s3[i] == s2[i_s2] and dp(i+1, i_s1, i_s2+1)

        #     if i_s2 == len(s2):
        #         return s3[i] == s1[i_s1] and dp(i+1, i_s1+1, i_s2)

        #     if s3[i] == s1[i_s1] and s3[i] == s2[i_s2]:
        #         return dp(i+1, i_s1+1, i_s2) or dp(i+1, i_s1, i_s2+1)
        #     elif s3[i] == s1[i_s1]:
        #         return dp(i+1, i_s1+1, i_s2)
        #     elif s3[i] == s2[i_s2]:
        #         return dp(i+1, i_s1, i_s2+1)

        #     return False
    
        # if len(s3) != len(s1) + len(s2):
        #     return False
        # return dp(0, 0, 0)