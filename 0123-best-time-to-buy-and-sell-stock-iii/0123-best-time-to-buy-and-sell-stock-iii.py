class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        prices[i] i day
        maximum profit
        at most 2 transactions -> buy and sell?
        # in a day, I can do buy, sell, or skip
        """
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



