class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {'6': 9, '9': 6, '1': 1, '0': 0, '8': 8}

        s = 0
        for n in num[::-1]:
            s *= 10

            if not n in strobogrammatic:
                return False

            s += strobogrammatic[n]
        return str(s) == num
        