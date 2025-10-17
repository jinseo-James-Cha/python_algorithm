class Solution:
    def isHappy(self, n: int) -> bool:
        used = set()
        while n > 1:
            temp = 0
            while n > 0:
                remainder = n % 10
                temp += remainder**2
                n //= 10
            if temp in used:
                return False
            used.add(temp)
            n = temp
        return True if n == 1 else False            