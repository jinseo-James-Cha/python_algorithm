

# IN OUT
# 1  1
# 2  2
# 3  3
# 4  5  
# example of 4 steps
# 1111
# 121
# 112
# 211
# 22
# is it finonacci sequence ?!

class Solution:
    def climbStairs(self, n: int) -> int:
        # top-down without memoization -> time limit exceeded
        cache = [-1] * 46
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        def fibo(n):
            if cache[n] > -1:
                return cache[n]
            else:
                cache[n] = fibo(n-2) + fibo(n-1)
            return cache[n]
        return fibo(n)
        