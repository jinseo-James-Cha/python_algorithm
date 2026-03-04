class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        curr_score = 0

        for ch in s:
            if ch == "(":
                curr_score += 1
            else:
                if curr_score > 0:
                    curr_score -= 1
                else:
                    res += 1
        
        res += curr_score
        return res