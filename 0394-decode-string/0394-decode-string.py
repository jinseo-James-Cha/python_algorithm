class Solution:
    def decodeString(self, s: str) -> str:
        # 3 [ a 2 [c] ]
        # 3[a cc ]


        # 3a2c
        # 3acc
        # accaccacc

        # 3[a2[c]]
        # 
        # 3[a]2[bc]
        # 3a2bc
        # 3abcbc
        # 3ab

        stack = [] # 3[a
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                
                stack.pop()

                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                
                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)
