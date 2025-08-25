class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # maximum profit
        # transaction fee = -2
        
        # state
        # days -> i
        # action -> buy or skip / sell or skip

        # bottom up optimize
        hold = -prices[0]
        free = 0
        for i in range(1, len(prices)):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        
        return free





        # bottom up
        dp_hold = [0] * len(prices)
        dp_free = [0] * len(prices)

        dp_hold[0] = -prices[0]
        for i in range(1, len(prices)):
            dp_hold[i] = max(dp_hold[i-1], dp_free[i-1] - prices[i]) # 어제꺼 홀딩 or 지금 매수
            dp_free[i] = max(dp_free[i-1], dp_hold[i-1] + prices[i] - fee) # 어제꺼 그대로, 매도
        return dp_free[-1]



        # top down
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