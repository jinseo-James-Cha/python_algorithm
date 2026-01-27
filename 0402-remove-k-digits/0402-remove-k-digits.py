class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Greedy with stack
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        final_stack = stack[:-k] if k else stack
        return "".join(final_stack).lstrip('0') or "0"


        # remove k digits from all num...
        # check all combinations?
        # backtrack.. -> Memory over flow..

        # edge case 
        if len(num) == k:
            return "0"

        smallest_possible_integer = float('inf')
        def backtrack(curr, start):
            nonlocal smallest_possible_integer
            if len(curr) == len(num) - k:
                smallest_possible_integer = min(smallest_possible_integer, int("".join(curr)))
                return

            for i in range(start, len(num)):
                curr.append(num[i])
                backtrack(curr, i+1)
                curr.pop()
                
        backtrack([], 0)
        return str(smallest_possible_integer)