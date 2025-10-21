class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in parentheses:
                stack.append(c)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr != parentheses[c]:
                    return False
        
        return not stack