class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = "+"

        for ch in s + "+":
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-*/":
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack[-1] *= num
                elif prev_op == "/":
                    stack[-1] = int(stack[-1] / num)

                num = 0
                prev_op = ch

        return sum(stack)