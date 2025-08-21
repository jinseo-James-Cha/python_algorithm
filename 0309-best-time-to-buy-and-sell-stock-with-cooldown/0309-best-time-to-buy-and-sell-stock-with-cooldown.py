class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state
        # days -> i
        # action -> 0 buying, 1 selling

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