class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        curr = ""
        for i in range(len(s)):
            if s[i] != " ":
                curr += s[i]
            elif curr:
                stack.append(curr)
                curr = ""
        
        # curr still has the last word
        res = ""
        res += curr + " " if curr else ""
        while stack:
            res += stack.pop() + " "
        
        return res[:-1]