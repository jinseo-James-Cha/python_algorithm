class Solution:
    def numDecodings(self, s: str) -> int:
        """
        decode ways

                        11106
                    1    1106             11 106
                   A  1    106         11 06 
                      A   1 "06" 10 6
                                 J  F ....
        
        starting from 0 -> nope
        valid range "1" <= ch <= "26" -> ways -> always same result
        I can break down into subproblems
        like 112 -> 1 , 12 -> dynamic programing
        state i?
        choice 2 1split or 2split
        """

        # state
        # string and its index s[i:]
        # decode complete? i == len(s)

        # how to distinguish 06 -> two letter should be 10~26
        # one letter should be 1 ~ 26

        # action choose 1letter or 2letters

        # 1 1 1 0 6 -> 1 / 1106 + 11 / 106

        # bottom up
        dp = [0] *(len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]








        # top down
        # dp(0) -> dp(1) + dp(2)
        def dp(i):
            if i == len(s):
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

        """
        return the number of ways to decode a string

        it can decode 1 character or 2 characters
        my possibilities = 1character decode ways + 2 characters decode ways

        """
        if len(s) == 1:
            return 1 if s[0] != "0" else 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            
            two_digits = int(s[i-2: i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
            
        return dp[-1] 


        def dp(i):
            if i == len(s):
                return 1
            
            # there is no start with 0
            if s[i] == "0":
                return 0
            
            if i not in memo:
                possibilities = dp(i+1)
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    possibilities += dp(i+2)
                memo[i] = possibilities

            return memo[i]
        
        memo = {}
        return dp(0)



        # state
        # string and its index s[i:]
        # decode complete? i == len(s)

        # how to distinguish 06 -> two letter should be 10~26
        # one letter should be 1 ~ 26

        # action choose 1letter or 2letters

        # bottom up
        if len(s) == 1:
            return 0 if s[0] == "0" else 1

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            
            two_digits = int(s[i-2: i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
            
        return dp[-1]
        

        
        # top down
        def dp(i):
            if i == len(s):
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
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i]) * 10 + int(s[i+1]) <= 26:
                res += dfs(i + 2)                    
            
            memo[i] = res
            return memo[i]
        
        memo = {}
        return dp(0)