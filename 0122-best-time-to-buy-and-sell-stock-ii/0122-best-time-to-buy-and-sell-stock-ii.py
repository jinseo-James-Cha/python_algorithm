# V2 - I don't need Sliding window or two pointer for this question...
# like the below
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit

# let me start with Two pointer and then I will study sliding window. good.
# let's gogogo

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         answer = 0
        
#         left = 0
#         for right in range(1, len(prices)):
#             if prices[left] < prices[right]:
#                 answer += prices[right] - prices[left]
#             left += 1
#         return answer