class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = float(-inf)
        res = ""

        for i in range(3, len(num)+1):
            digit = num[i-3:i]
            s = set(digit)
            print(s)
            if len(s) == 1:
                int_digit = int(digit)
                if max_num < int_digit:
                    max_num = int_digit
                    res = digit
        
        return res




                