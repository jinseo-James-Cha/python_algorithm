class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == " " and prev != " ":
                print(prev)
                res += 1
            prev = s[i]
        
        if s[-1] == " ":
            res -= 1
            
        return res if len(s) != res-1 else 0