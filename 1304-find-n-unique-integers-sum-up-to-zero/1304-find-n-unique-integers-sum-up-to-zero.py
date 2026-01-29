class Solution:
    def sumZero(self, n: int) -> List[int]:
        # len(array) == n with unique integer? sum(arr) == 0
        

        # n 
        # 1  2   3       4          5
        # 0 -1,1 -1 0 1  -2 -1 1 2  -2 -1 0 1 2

        # bottom up
        if n == 1:
            return [0]

        dp = [[] for _ in range(n+1)]
        dp[1] = [0]
        for i in range(2, n+1):
            dp[i] = dp[i-2] + [i//2] + [-(i//2)]
        return dp[n]

        

        # top down
        def dp(i):
            if i == 0:
                return []
            elif i == 1:
                return [0]
            
            if i not in memo:
                curr_val = i // 2
                memo[i] = dp(i-2) +  [-curr_val, curr_val]
            
            return memo[i]

        memo = {}
        return dp(n)
        


