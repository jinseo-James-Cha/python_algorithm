# let me start with Two pointer and then I will study sliding window. good.
# let's gogogo

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        left = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                answer += prices[right] - prices[left]
            left += 1
        return answer