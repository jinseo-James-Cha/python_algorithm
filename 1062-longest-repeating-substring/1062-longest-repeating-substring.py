class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # brute force
        # check all substrings and it exists in a set it is repeating substring and return the max len
        substrings = set()
        max_len = 0
        for i in range(len(s)):
            
            curr = s[i]
            if curr not in substrings:
                substrings.add(curr)
            elif max_len < 1:
                max_len = 1
            
            for j in range(i+1, len(s)):
                curr += s[j]
                if curr not in substrings:
                    substrings.add(curr)
                elif max_len < len(curr):
                    max_len = len(curr)
        return max_len

















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
