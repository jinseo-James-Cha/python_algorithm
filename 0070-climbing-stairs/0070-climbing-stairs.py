class Solution:
    def climbStairs(self, n: int) -> int:
        # top-down
        # 1 -> 1
        # 2 -> 1 + 1
        # n에 도착하는 방법은 n-1에서 오거나 n-2에서 오거나
        # 그러므로 n = n-1의 경우의 수 + n-2의 경우의 수

        def cal_stairs(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = cal_stairs(n-1) + cal_stairs(n-2)
            return memo[n]
        
        memo = {}
        return cal_stairs(n)
        









        # v2: bottom-up
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        # v1: top-down -> TLE
        # memo = {}

        # if n <= 2:
        #     return n
        # if n in memo:
        #     return memo[n]
        
        # memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # return memo[n] 
        

