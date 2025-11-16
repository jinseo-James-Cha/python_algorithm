class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        res = 0

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                new_num = 0
                if token == '+':
                    new_num = first_num + second_num
                elif token == '-':
                    new_num = first_num - second_num
                elif token == '*':
                    new_num = first_num * second_num
                else:
                    new_num = int(first_num / second_num)
                stack.append(new_num)
                
        return stack[-1]

            