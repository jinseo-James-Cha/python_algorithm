class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1

        while n > 1:
            i += 1
            n //= 2
        return 2**i - 1