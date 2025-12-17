class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dp(day, transactionNumber, state):
            if transactionNumber == 0:
                return 0
            
            if day == 0:
                return 0 if state == 0 else -prices[0] if state == 1 else prices[0] 
            
            p = prices[day]
            if state == 0:
                res = max(dp(day-1, transactionNumber, 0), dp(day-1, transactionNumber, 1) + p, dp(day-1, transactionNumber, 2) - p)
            elif state == 1:
                res = max(dp(day-1, transactionNumber, 1), dp(day-1, transactionNumber-1, 0) - p)
            else:
                res = max(dp(day-1, transactionNumber, 2,), dp(day-1, transactionNumber - 1, 0) + p)

            return res
        res = dp(n-1, k, 0)
        dp.cache_clear()
        return res