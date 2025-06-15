class Solution:
    def confusingNumber(self, n: int) -> bool:
        confuses = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        res = 0
        origin = n
        while n > 0:
            res *= 10
            temp = n % 10
            if temp not in confuses:
                return False
            
            n //= 10
            res += confuses[temp]
            

        return res != origin