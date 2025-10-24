class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # n,m > 0
        # num1 => sum range(1 , n+1) where % m != 0
        # num2 => sum range(1, m+1) where % m == 0
        num1, num2 = 0, 0
        for i in range(1, n+1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2
