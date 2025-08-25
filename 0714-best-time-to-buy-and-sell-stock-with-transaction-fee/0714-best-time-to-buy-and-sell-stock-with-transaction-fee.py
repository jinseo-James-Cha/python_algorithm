class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # maximum profit
        # transaction fee = -2
        
        # state
        # days -> i
        # action -> buy or skip / sell or skip

        def dp(i, holding):
            if i == len(prices):
                return 0
    
            if (i, holding) not in memo:
                doNothing = dp(i+1, holding)
                doSomething = 0
                # sell already hold, 
                if holding:
                    doSomething = (prices[i] - fee) + dp(i+1, 0)
                else: # buying stock
                    doSomething = -prices[i] + dp(i+1, 1)

                memo[(i, holding)] = max(doNothing, doSomething)
            return memo[(i, holding)]
        
        memo = {}
        return dp(0, 0)