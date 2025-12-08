class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # maximum profit -> dp?
        # dp top down
        def dp(day, transactionTime, isHoldingStock):
            nonlocal k
            if day == len(prices):
                return 0
            
            if transactionTime == k:
                return 0

            if (day, transactionTime, isHoldingStock) not in memo:
                doNothing = dp(day + 1, transactionTime, isHoldingStock)
                doSomething = 0
                if isHoldingStock:
                    doSomething = prices[day] + dp(day+1, transactionTime+1, False)
                else:
                    doSomething = -prices[day] + dp(day+1, transactionTime, True)
                memo[(day, transactionTime, isHoldingStock)] = max(doNothing, doSomething)
            return memo[(day, transactionTime, isHoldingStock)]
        
        memo = {}
        return dp(0, 0, False)
        


        # state 
        # - which day -> i
        # - transaction number -> k
        # - action -> buy or sell or nothing
        
        # bottom up 3D
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        # dp[n][k][buying]

        for i in range(n-1, -1, -1):
            for transaction_remaining in range(1, k+1):
                for holding in range(2):
                    doNothing = dp[i+1][transaction_remaining][holding]
                    if holding:
                        doSomething = prices[i] + dp[i + 1][transaction_remaining - 1][0]
                    else:
                        doSomething = -prices[i] + dp[i + 1][transaction_remaining][1]
                    dp[i][transaction_remaining][holding] = max(doNothing, doSomething)
        
        return dp[0][k][0]


        # top down
        def dp(i, transactionTime, holdingStock):
            # two base cases
            if i == len(prices):
                return 0
            if transactionTime == k:
                return 0
            
            if (i, transactionTime, holdingStock) not in memo:
                doNothing = dp(i+1, transactionTime, holdingStock)
                doSomething = 0
                # can sell if holding a stock
                if holdingStock:
                    doSomething = prices[i] + dp(i+1, transactionTime + 1, False)
                else:
                    doSomething = -prices[i] + dp(i+1, transactionTime, True)
                memo[(i, transactionTime, holdingStock)] = max(doNothing, doSomething)

            
            return memo[(i, transactionTime, holdingStock)]

        memo = {}
        return dp(0, 0, False)
                
            

