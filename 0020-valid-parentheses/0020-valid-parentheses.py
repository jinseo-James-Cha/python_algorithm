class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in parentheses:
                stack.append(p)
            else:
                if not stack:
                    return False
                    
                poped = stack.pop()
                if parentheses[poped] != p:
                    return False
        return not stack