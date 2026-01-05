class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        return Maximum profit
        unlimited transaction with fee.
        state = which day, holding stock?

        t1: sell price - buy price - fee + t2: ...
        """
        def dp(i, is_holding):
            if i == len(prices):
                return 0
            
            if (i, is_holding) not in memo:
                # skip - do nothing
                do_nothing = dp(i+1, is_holding)
                do_something = 0
                
                # time to sell
                if is_holding:
                    do_something = prices[i] + dp(i+1, False) - fee
                else:# buy
                    do_something = -prices[i] + dp(i+1, True)
                
                memo[(i, is_holding)] = max(do_nothing, do_something)

            return memo[(i, is_holding)]
        
        memo = {}
        return dp(0, False)
