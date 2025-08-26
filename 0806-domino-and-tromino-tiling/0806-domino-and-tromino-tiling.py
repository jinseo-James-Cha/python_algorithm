class Solution:
    def numTilings(self, n: int) -> int:
        # state
        # n
        MOD = 10**9 + 7
        memo = {}
        
        def dp(size):
            if size <= 1:
                return 1

            if size == 2:
                return 2

            if size not in memo:
                memo[size] = (dp(size-1) + dp(size-2) + 2*sum(dp(i) for i in range(size-3+1))) % MOD
            return memo[size]
        
        return dp(n)

        