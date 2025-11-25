from collections import Counter
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # Calculate n!
        n_factorial = 1
        for i in range(2, n + 1):
            n_factorial *= i
        
        res = 0
        while n_factorial % 10 == 0:
            res += 1
            n_factorial //= 10
        return res