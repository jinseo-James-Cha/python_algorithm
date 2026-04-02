class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        maximum profit
        # cannot buy the day after you sell stock
        -> sell stock -> day + 2

        state = day, is_hold
        """
        def dp(day, is_hold):
            if day >= len(prices):
                return 0
            
            if (day, is_hold) not in memo:
                do_nothing = dp(day+1, is_hold)
                do_something = 0
                if is_hold:
                    do_something = dp(day+2, False) + prices[day]
                else:
                    do_something = dp(day+1, True) - prices[day]

                memo[(day, is_hold)] = max(do_nothing, do_something)       
            return memo[(day, is_hold)]

        memo = {}
        return dp(0, False)
















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