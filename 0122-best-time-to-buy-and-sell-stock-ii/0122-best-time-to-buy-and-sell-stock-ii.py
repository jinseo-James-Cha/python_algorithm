class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, isHoldingStock):
            if i == len(prices):
                return 0
            
            # two decision by isHoldingStock
            do_nothing = dp(i+1, isHoldingStock) 
            do_something = 0
            if isHoldingStock:
                # sell
                do_something = dp(i+1, False) + prices[i]
            else:
                do_something = dp(i+1, True) - prices[i]
            
            return max(do_nothing, do_something)



        return dp(0,False)

                