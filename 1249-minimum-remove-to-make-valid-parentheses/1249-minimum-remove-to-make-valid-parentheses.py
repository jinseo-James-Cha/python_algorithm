class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_indices = []
        good_indices = set()

        for i, ch in enumerate(s):
            if ch != "(" and ch != ")":
                good_indices.add(i)
            elif ch == "(":
                open_indices.append(i)
            else:
                if not open_indices:
                    continue
                
                good_indices.add(open_indices.pop())
                good_indices.add(i)
        
        res = ""
        for i, ch in enumerate(s):
            if i in good_indices:
                res += ch
        return res













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
        