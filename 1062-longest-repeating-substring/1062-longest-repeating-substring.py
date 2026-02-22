class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
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
