class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # step 1
        # remove whitespace
        s = s.lstrip(" ")

        if len(s) == 0:
            return 0

        sign = 1
        res = 0
        for i, ch in enumerate(s):
            # step 2
            if ch == "+" or ch == "-":
                if i != 0:
                    break
                
                if ch == "-":
                    sign = -1
                continue

            # step 3
            if ch == "0":
                if res == 0:
                    continue
            
            if not ch.isnumeric():
                break

            digit = int(ch)
            # step 4
            if (res > INT_MAX // 10) or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = 10 * res + digit

        return sign * res
