class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # maximum profit -> dp?

        # state 
        # - which day -> i
        # - transaction number -> k
        # - action -> buy or sell or nothing

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
                
            

