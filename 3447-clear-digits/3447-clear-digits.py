class Solution:
    def clearDigits(self, s: str) -> str:
        # remove all digits 
        # delete first digit and next left character(non digit)
        
        # ab12 -> ""
        # ab1c -> ac
        # abcd -> abcd
        # 1a23 -> 13
        # a123 -> 23
        # 1ab3 -> 1a
        # a1b3 -> ""
        
        # stack!!!!!!!!
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                stack.pop()
        
        return ''.join(stack)