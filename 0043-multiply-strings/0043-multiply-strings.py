class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        #     1 2 3
        #   x   4 5
        #         i = 2 j = 1
        # 
        # i = 2 ~ 0 j = 1 ~ 0
        # result 0 0 0 0 0

        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                curr = int(num1[i]) * int(num2[j])

                curr_position = i + j + 1
                next_position = i + j

                total = curr + result[curr_position]
                result[curr_position] = total % 10
                result[next_position] += total // 10

        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        return ''.join(map(str, result[i:])) or "0"

        