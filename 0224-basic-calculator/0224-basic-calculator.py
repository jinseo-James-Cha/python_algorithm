# wanna do this again later
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num, sign, res = 0, 1, 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '+' or c == '-':
                res += curr_num * sign
                sign = -1 if c == '-' else 1
                curr_num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * curr_num
                
                res *= stack.pop()
                res += stack.pop()
                curr_num = 0
        return res + curr_num * sign