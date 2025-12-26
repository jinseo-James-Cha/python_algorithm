class Solution:
    def removeStars(self, s: str) -> str:
        # stack
        stack = []
        for ch in s:
            if ch == "*" and stack:
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)