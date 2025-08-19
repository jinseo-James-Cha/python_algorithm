class Solution:
    def tribonacci(self, n: int) -> int:
        # bottom up tabulation
        if n == 0:
            return 0
        if n <= 2:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]


        # top down memoization
        # if n == 0:
        #     return 0
        
        # def dp(i):
        #     if i <= 0 :
        #         return 0
        #     if i <= 2:
        #         return 1
        #     if i not in memo:
        #         memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
        #     return memo[i]
        
        # memo = {}
        # return dp(n)








#         if n == 0:
#             return 0

#         memo = [0] * (n + 2)
#         memo[1] = memo[2] = 1
#         if n <= 2:
#             return memo[n]

#         for i in range(3, n+1):
#             memo[i] = memo[i-3] + memo[i-2] + memo[i-1]
#         return memo[n]