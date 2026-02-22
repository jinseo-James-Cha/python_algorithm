class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force o(n**2)
        # first loop from the beginner 
        # second loop from i + 1
        # move right until s[i] == s[j]-> j-i+1

        # optimize
        # sliding window
        # abca
        #  L A
        # add one by one in set
        
        # remove s[left] until s[right] not in set

        longest_len = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            longest_len = max(longest_len, len(seen))
        return longest_len
