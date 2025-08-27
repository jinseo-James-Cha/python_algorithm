class Solution:
    def numTilings(self, n: int) -> int:
        # state
        # n

        # the candidates who can come at the end of the tiles
        # |
        # -
        # ㄱ
        # ㅢ




        MOD = 10**9 + 7
        F, T, B = {0:1, 1: 1}, {1: 0}, {1 : 0}
        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2] + T[i-1] + B[i-1]
            T[i] = B[i-1] + F[i-2]
            B[i] = T[i-1] + F[i-2]
        return F[n] % MOD









        # top down
        @cache
        def dp(i, previous_full):
            if i > n:
                return 0
            if i == n:
                if previous_full:
                    return 1
                else:
                    return 0
            
            if not previous_full:
                return dp(i+1, True) + dp(i+1, False)

            return dp(i+1, True) + dp(i+2, True) + dp(i+2, False)*2
        
        return dp(0, True) % MOD

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

        