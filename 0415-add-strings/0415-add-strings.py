# ord makes str to int
# chr makes int to str
# alphabet ord(a) - ord('a')
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        l_n1 = len(num1) - 1
        l_n2 = len(num2) - 1
        while l_n1 >= 0 or l_n2 >= 0:
            x1 = ord(num1[l_n1]) - ord('0') if l_n1 >= 0 else 0
            x2 = ord(num2[l_n2]) - ord('0') if l_n2 >= 0 else 0

            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            l_n1 -= 1
            l_n2 -= 1
        
        if carry:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])