class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state
        # days -> i
        # action -> holding? yes -> sell or skip / no -> buying or skip

        if len(prices) == 1:
            return 0

        buying_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buying_price)
            buying_price = min(buying_price, prices[i])
        return max_profit

