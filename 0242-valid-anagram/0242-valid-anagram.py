from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s_c = Counter(s)
        t_c = Counter(t)

        for k, v in s_c.items():
            if not k in t_c:
                return False
            elif not s_c[k] == t_c[k]:
                return False
        
        return True
        