class Solution:
    def countSubstrings(self, s: str) -> int:
        # v2: DP
        res = 0
        n = len(s)

        if n == 0:
            return 0

        dp = [[False] * n for _ in range(n)]
        
        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        # Base case: double letter substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1
        
        # Substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1

        return res





        # 1. intuition
        # brute force,
        # len += 1 and looping all possible cases

        # 2. complexity
        # time: o(n^3) -> 1000 -> TLE

        # 3. data structure
        # str: temp
        # int: res

        # res = 0
        # for length in range(1, len(s) + 1):
        #     for i in range(len(s)+1 - length):
        #         temp = s[i:length+i]
        #         i = 0
        #         j = len(temp) - 1
        #         is_palindromic = True
        #         while i < j:
        #             if temp[i] != temp[j]:
        #                 is_palindromic = False
        #                 break
        #             i += 1
        #             j -= 1

        #         if is_palindromic:
        #             res += 1
        # return res
