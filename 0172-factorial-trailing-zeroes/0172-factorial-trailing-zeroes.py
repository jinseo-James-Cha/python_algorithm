from collections import Counter
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fatorial(n: int):
            if n <= 2:
                return n
            
            return fatorial(n-1) + factorial(n-2)
        
        num = factorial(n)
        
        res = 0
        while num > 0:
            if num % 10 != 0:
                break
            res += 1
            num //= 10
        return res