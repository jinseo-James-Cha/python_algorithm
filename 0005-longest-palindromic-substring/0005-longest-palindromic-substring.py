class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. intuition
        # stack? sliding window? two pointers?
        # Brute force will be ok cuz of lenth 1000.
        # nested loop for each and save longest and compare len 

        # 2. complexity
        # time - o(n^2)
        # space - o(1)

        # 3. data structure
        # str - res, current
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(len(s), i, -1):
                if j - i < len(res):
                    break
                current = s[i:j]
                check_i = 0
                palindromic = True
                while check_i < len(current) // 2 :
                    if current[check_i] != current[~check_i]:
                        palindromic = False
                        break
                    check_i += 1
                
                if palindromic:
                    if len(res) < len(current):
                        res = current
        return res


        


