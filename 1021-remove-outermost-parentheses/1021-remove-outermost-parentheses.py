class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if len(s) <= 2:
            return ""
        
        primitives = []
        curr_score = 0
        left = 0
        for right, ch in enumerate(s): # (()()) (()) 121210 left = 0 right = 5 left = 6
            if ch == "(":
                curr_score += 1
            else:
                curr_score -= 1
            
            if curr_score == 0:
                primitives.append(s[left:right+1]) # s[0:5+1]
                left = right+1 # left = 6
        
        res = ""
        for primitive in primitives:
            res += primitive[1:len(primitive)-1]
        return res