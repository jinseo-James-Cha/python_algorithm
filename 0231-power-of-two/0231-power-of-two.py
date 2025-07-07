class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        if n == 1:
            return True

        # 16 8 4 2 0 -> True
        # 3 1.5 -> False
        # 6 3 1.5 -> False
        # 8 4 2 0
        # 10 5 2.5
        while n > 1:
            print(n, n % 2)
            if n % 2 != 0:
                return False
            n //= 2
        return True
