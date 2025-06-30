class Solution:
    def removeDuplicates(self, s: str) -> str:
        # adjacent -> stack?!
        # using stack 
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
                continue
            
            stack.append(ch)
        return ''.join(stack)

