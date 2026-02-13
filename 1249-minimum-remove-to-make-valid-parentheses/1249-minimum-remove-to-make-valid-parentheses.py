class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parenthese = 0
        pairs = 0
        for ch in s:
            if ch == "(":
                open_parenthese += 1
            elif ch == ")" and open_parenthese > 0:
                pairs += 1
                open_parenthese -= 1
        
        # add ( and ) as much as pairs
        open_used = pairs
        res = ""
        for ch in s:
            if ch != "(" and ch != ")":
                res += ch
            elif ch == "(" and pairs > 0 and open_used > 0:
                open_used -= 1
                res += ch
            elif ch == ")" and pairs > 0 and open_used < pairs:
                res += ch
                pairs -= 1
        return res
        