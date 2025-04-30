# LIFO -> Stack?!

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        for a in s:
            if a == "#":
                if stack_a:
                    stack_a.pop()
            else:
                stack_a.append(a)

        stack_b = []
        for b in t:
            if b == "#":
                if stack_b:
                    stack_b.pop()
            else:
                stack_b.append(b)

        return stack_a == stack_b
        