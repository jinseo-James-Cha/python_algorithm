class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # dp
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        max_length = 0

        for i in range(1, length + 1):
            for j in range(i + 1, length + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length


        # brute force
        # o(n**3) o of cubed 
        curr_size = len(s) - 1

        for size in range(len(s) - 1, 0, -1):
            seen = set()
            for i in range(len(s) - size+1):
                end = i
                curr_sub = s[end: end+size]
                if curr_sub in seen:
                    return size
                
                seen.add(curr_sub)
        
        return 0
