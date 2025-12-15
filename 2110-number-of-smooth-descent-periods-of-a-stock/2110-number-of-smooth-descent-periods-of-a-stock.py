class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # dp
        n = len(prices)
        res = 1
        prev = 1
        for i in range(1, n):
            if prices[i] == prices[i-1] -1:
                prev += 1
            else:
                prev = 1
            res += prev
        return res


        n = len(prices)
        curr = [prices[0]]
        descents = []
        for i in range(1, n):
            if curr[-1] == prices[i] + 1:
                curr.append(prices[i])
            else:
                descents.append(curr[:])
                curr = [prices[i]]
        if curr:
            descents.append(curr[:])
        
        # 3 -> 1 -> 1
        # 32 -> 2 + 1 -> 3
        # 321 -> 3 + 2 + 1  -> 6
        # 3210 -> 4 + 3 + 2 + 1 -> 10
        res = 0
        for d in descents:
            size = len(d)
            for i in range(1, size+1):
                res += i
        return res



        # 1 combi
        # res = n 
        
        # # 2 combi
        # for i in range(n-1): 
        #     if prices[i] == prices[i+1] + 1:
        #         res += 1
        
        # # 3 2 1 4
        # # L
        # # R
        # left = 0
        # for right in range():
        #     if prices[right] + 1 == prices[right-1]:

        #     res += 1
