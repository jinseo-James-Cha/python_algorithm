# 1 <= s.length <= 10**5

# TLE caused
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # using built in functions
        d = {}
        for i in range(len(s)):
            if s[i] in d and len(d[s[i]]) >= 2:
                continue
            d[s[i]] = d.get(s[i], []) + [i]
        
        for v in d.values():
            if len(v) == 1:
                return v[0]

        return -1
        