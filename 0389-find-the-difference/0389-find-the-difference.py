class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
        
        for j in range(len(t)):
            if t[j] not in counter:
                return t[j]
            if counter[t[j]] == 0:
                return t[j]
            
            counter[t[j]] -= 1
        return -1
