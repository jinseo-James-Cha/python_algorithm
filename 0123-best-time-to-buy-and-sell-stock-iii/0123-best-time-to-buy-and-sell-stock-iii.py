class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        prices[i] i day
        maximum profit
        at most 2 transactions -> buy and sell?
        # in a day, I can do buy, sell, or skip
        """
        # dp bottom up
        n = len(prices)
        # dp[day][transactionRemaining][isHolding]
        dp = [[[0] * 2 for _ in range(3)] for __ in range(n + 1)]
        for day in range(n-1, -1, -1):
            for transactionRemaining in range(1, 3):
                for isHolding in range(2):
                    doNothing = dp[day+1][transactionRemaining][isHolding]
                    doSomething = 0
                    if isHolding:
                        doSomething = prices[day] + dp[day+1][transactionRemaining-1][0]
                    else:
                        doSomething = -prices[day] + dp[day+1][transactionRemaining][1]
                    dp[day][transactionRemaining][isHolding] = max(doNothing, doSomething)
        return dp[0][2][0]


        # dp top down
        def dp(day, transactionTime, isHolding):
            if day == len(prices):
                return 0
            if transactionTime == 2:
                return 0
            
            if (day, transactionTime, isHolding) not in memo:
                doNothing = dp(day + 1, transactionTime, isHolding)
                doSomething = 0
                if isHolding:
                    doSomething = prices[day] + dp(day+1, transactionTime+1, False)
                else:
                    doSomething = -prices[day] + dp(day+1, transactionTime, True)
                memo[(day, transactionTime, isHolding)] = max(doNothing, doSomething)
            return memo[(day, transactionTime, isHolding)]

        memo = {}
        return dp(0, 0, False)



