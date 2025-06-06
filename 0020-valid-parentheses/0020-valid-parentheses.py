class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        if len(s) % 2 != 0:
            return False
        
        for b in s:
            if b in open_brackets:
                open_stack.append(b)
            else:
                if not open_stack:
                    return False
                    
                bracket = open_stack.pop()
                if bracket != open_brackets[close_brackets.index(b)]:
                    return False
        return not open_stack

