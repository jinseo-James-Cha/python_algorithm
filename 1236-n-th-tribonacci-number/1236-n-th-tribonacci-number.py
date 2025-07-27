class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        memo = [0] * (n + 2)
        memo[1] = memo[2] = 1
        if n <= 2:
            return memo[n]

        for i in range(3, n+1):
            memo[i] = memo[i-3] + memo[i-2] + memo[i-1]
        return memo[n]