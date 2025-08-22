class Solution:
    def numDecodings(self, s: str) -> int:
        # state
        # string and its index s[i:]
        # decode complete? i == len(s)

        # how to distinguish 06 -> two letter should be 10~26
        # one letter should be 1 ~ 26

        # action choose 1letter or 2letters
        
        def dp(i):
            if i == len(s): # I think even tho its over the len, it is still true..
                return 1
            
            if s[i] == "0":
                return 0
            
            if i not in memo:
                one_letter = dp(i+1)
                two_letter = 0                    
                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:     
                    two_letter = dp(i+2)
                memo[i] = one_letter + two_letter
            return memo[i]
        
        memo = {}
        return dp(0)

        # dp(2-1)














        # bottom-up
        if len(s) == 1:
            return 1 if s[0] != "0" else 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

        # Top-down / memoization
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
            
        #     if i == len(s):
        #         return 1
            
        #     if s[i] == "0":
        #         return 0
            
        #     # 한 글자 해석
        #     res = dfs(i + 1)

        #     # 두 글자 해석 가능하면 더하기
        #     if i + 1 < len(s) and int(s[i]) * 10 + int(s[i+1]) <= 26:
        #         res += dfs(i + 2)                    
            
        #     memo[i] = res
        #     return memo[i]
        
        # memo = {}
        # return dfs(0)