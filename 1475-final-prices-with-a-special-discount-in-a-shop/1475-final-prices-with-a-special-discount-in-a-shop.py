class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # keep idx which has smaller than next elements
        res = prices[:]
        idx_stack = []
        for i in range(len(prices)):
            while idx_stack and prices[idx_stack[-1]] >= prices[i]:
                res[idx_stack.pop()] -= prices[i]
            idx_stack.append(i)
        return res

        # brute force
        res = [-1] * len(prices)
        for i in range(len(prices)):
            flag = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    res[i] = prices[i]-prices[j]
                    flag = True
                    break
            if not flag:
                res[i] = prices[i]
        return res
