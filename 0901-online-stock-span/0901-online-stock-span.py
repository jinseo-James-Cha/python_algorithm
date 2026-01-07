class StockSpanner:
    def __init__(self):
        self.span_price = [] # (price, day)

    def next(self, price: int) -> int:
        span = 1
        while self.span_price and self.span_price[-1][1] <= price:
            span += self.span_price.pop()[0]
        
        self.span_price.append((span, price))
        print(self.span_price)
        return span
            

    # brute force
    # def __init__(self):
    #     self.prev_prices = []

    # def next(self, price: int) -> int:
    #     span = 1
    #     for prev_price in reversed(self.prev_prices):
    #         if price >= prev_price:
    #             span += 1
    #         else:
    #             break
    #     self.prev_prices.append(price)
    #     return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
"""
return the span of that stock's price for the current day.
Span => stock's price in one day is the maximum number of consecutive days
starting from that day and going Backward for the stock price was less than or equal to

7 2    1 2
  here +1+1
0 1    2 3 -> or 3 - 1 ?
the price of the stock today is 2 -> the span of today is 4

7 34 1 2
if price is 8 today
the span -> 3

[[100], [80], [60], [70], [60], [75], [85]]
   1      1    1     2      1    4     6

stack= [100]
span = 1
stack[-1] 100 > curr 80 return span
100 8
"""