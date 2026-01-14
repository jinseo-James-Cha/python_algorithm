class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if len(s) <= 2:
            return ""
        
        res = ""
        curr_score = 0
        left = 0
        for right, ch in enumerate(s):
            if ch == "(":
                curr_score += 1
            else:
                curr_score -= 1
            
            if curr_score == 0:
                res += s[left+1:right] 
                left = right+1 
        return res