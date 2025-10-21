class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = {'+', '-', '*', '/'}
        res = 0
        for t in tokens:
            if t not in operators:
                nums.append(int(t))
            else:
                y = nums.pop()
                x = nums.pop()
                if t == '+':
                    nums.append(x + y)
                elif t == '-':
                    nums.append(x - y)
                elif t == '*':
                    nums.append(int(x * y))
                else:
                    nums.append(int(x / y))
        return nums[0]