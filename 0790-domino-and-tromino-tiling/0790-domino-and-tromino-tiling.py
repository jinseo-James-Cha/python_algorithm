class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # bottom up
        if n <= 2:
            return n
        
        full = [0] * (n+1)
        partial = [0] * (n+1)
        
        full[1] = 1
        full[2] = 2
        partial[2] = 1
        for i in range(3, n+1):
            full[i] = (full[i-2] + full[i-1] + (partial[i-1] * 2)) % MOD
            partial[i] = full[i-2] + partial[i-1]
        return full[n]


        # Top down
        def dp_partial(i):
            if i == 2:
                return 1
            
            if i not in p_memo:
                p_memo[i] = (dp_partial(i-1) + dp_full(i-2)) % MOD
            return p_memo[i]

        def dp_full(i):
            if i <= 2:
                return i
            
            if i not in f_memo:
                f_memo[i] = (dp_full(i-1) + dp_full(i-2) + 2 * dp_partial(i-1)) % MOD
            return f_memo[i]
        
        f_memo = {}
        p_memo = {}
        return dp_full(n)