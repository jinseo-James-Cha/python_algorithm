class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, curr_num, sign = 0, 0, 1

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '+' or ch == '-':
                res += curr_num * sign
                curr_num = 0
                sign = -1 if ch == '-' else 1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1
            elif ch == ")":
                res += curr_num * sign

                res *= stack.pop()
                res += stack.pop()

                curr_num = 0
                sign = 1
        return res + curr_num * sign