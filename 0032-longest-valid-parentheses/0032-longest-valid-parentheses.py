class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        longest valid
        -> check if it is valid -> update the longest length with current valid length
        -> valid? open count == close count -> %2 == 0
        """

        """

        stack
        """
        max_len = 0
        idx_stack = []
        idx_stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                idx_stack.append(i)
            else:
                idx_stack.pop()
                if not idx_stack:
                    idx_stack.append(i)
                else:
                    max_len = max(max_len, i - idx_stack[-1])
        return max_len










        """
        ideas
        - using stack to store valid parentheses..
        - (( open 2 != close 0 -> not valid
        - (() open 2 close 1 -> 1 valid pair -> 2

        if foudn the pair take out and pair += 1
        return pair * 2

        brute force check every cases
        -> o(n^3)
        """
        def isValid(check_s):
            if not check_s:
                return False
            
            stack = []
            for cs in check_s:
                if cs == "(":
                    stack.append("(")
                else:
                    if not stack:
                        return False
                    else:
                        poped = stack.pop()
            return not stack

        maxlen = 0
        for i in range(len(s)):
            for j in range(i+2, len(s) + 1, 2):
                if isValid(s[i:j]):
                    maxlen = max(maxlen, j - i)
        return maxlen