class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {'6': '9', '9': '6', '1': '1', '0': '0', '8': '8'}

        s = ""
        for n in num[::-1]:
            if not n in strobogrammatic:
                return False

            s += strobogrammatic[n]
        return s == num
        