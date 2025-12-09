class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        # abc
        #  bca
        #   cab
        #    abc
        #      cb
        #        b
        # two pointers
        left = 0
        curr_set = set() # no dup
        res = 0
        for curr_ch in s:
            while curr_ch in curr_set:
                curr_set.remove(s[left])
                left += 1
            
            curr_set.add(curr_ch)
            res = max(res, len(curr_set))
        return res