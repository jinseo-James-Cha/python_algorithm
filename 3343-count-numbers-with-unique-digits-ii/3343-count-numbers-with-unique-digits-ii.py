class Solution:
    def numberCount(self, a: int, b: int) -> int:
        res = 0
        for i in range(a, b + 1):
            str_i = str(i)
            if len(set(str_i)) == len(str_i):
                res += 1
        return res