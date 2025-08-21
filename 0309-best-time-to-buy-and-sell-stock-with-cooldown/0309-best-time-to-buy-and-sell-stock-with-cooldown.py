class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state
        # days -> i
        # action -> 0 buying, 1 selling

        # bottom up
        dp = [[0] * 2 for _ in range(len(prices) + 2)]

        for i in range(len(prices)-1, -1, -1):
            for holding in range(2):
                doNothing = dp[i+1][holding]
                doSomething = 0
                if holding:
                    doSomething = prices[i] + dp[i+2][0]
                else:
                    doSomething = -prices[i] + dp[i+1][1]
                dp[i][holding] = max(doNothing, doSomething)
        
        return dp[0][0]





        # top down
        def dp(i, holding):
            if i >= len(prices):
                return 0
        
            if (i, holding) not in memo:
                # cooldown
                doNothing = dp(i+1, holding)
                
                doSomething = 0
                if holding:
                    doSomething = prices[i] + dp(i+2, 0) # selling 
                else:
                    doSomething = -prices[i] + dp(i+1, 1) # buying
                memo[(i, holding)] = max(doNothing, doSomething)
            return memo[(i, holding)]
        
        memo = {}
        return dp(0, 0) 