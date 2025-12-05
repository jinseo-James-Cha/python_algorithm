class Solution:
    def longestPalindrome(self, s: str) -> str:
        # babad
        # b left right and left >= 0 and right <= len(s)
        # keeping expanding til its end index or not matched

        def findPalindrome(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        res = ""
        for i in range(len(s)):
            even_palindrome = findPalindrome(i, i+1, s)
            odd_palindrome = findPalindrome(i, i, s)

            if len(res) < len(even_palindrome):
                res = even_palindrome
            
            if len(res) < len(odd_palindrome):
                res = odd_palindrome

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1: right]
        

        longest = ""
        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)
            if len(longest) < len(odd):
                longest = odd
            if len(longest) < len(even):
                longest = even

        return longest


        # dp
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # max_len = 1
        # start_index = 0
        # for i in range(n):
        #     dp[i][i] = True
        
        # for i in range(n-1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i+1] = True
        #         max_len = 2
        #         start_index = i
        
        # for substring_len in range(3, n + 1):
        #     for i in range(n - substring_len + 1):
        #         j = i + substring_len - 1

        #         if s[i] == s[j] and dp[i+1][j-1]:
        #             dp[i][j] = True
        #             max_len = substring_len
        #             start_index = i
        return s[start_index : start_index + max_len]







        # 1. intuition
        # stack? sliding window? two pointers?
        # Brute force will be ok cuz of lenth 1000.
        # nested loop for each and save longest and compare len 

        # 2. complexity
        # time - o(n^3)
        # space - o(n^2)

        # 3. data structure
        # str - res, current
        # res = s[0]
        # for i in range(len(s) - 1):
        #     for j in range(len(s), i, -1):
        #         if j - i < len(res):
        #             break
        #         current = s[i:j]
        #         check_i = 0
        #         palindromic = True
        #         while check_i < len(current) // 2 :
        #             if current[check_i] != current[~check_i]:
        #                 palindromic = False
        #                 break
        #             check_i += 1
                
        #         if palindromic:
        #             if len(res) < len(current):
        #                 res = current
        # return res