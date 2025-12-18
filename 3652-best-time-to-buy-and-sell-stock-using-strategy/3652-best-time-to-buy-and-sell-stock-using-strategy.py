class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # k % 2 == 0
        # one modification..
        # select k consecutive elements in strategy
        # first half (k / 2) -> 0(hold)
        # second half (k / 2) -> 1(sell)
        # profit = sum(strategy[i] * prices[i])

        # p[4, 2 ,8] s[-1,0,1] k: 2
        # original -> 4*-1 + 2*0 + 8*1 -> 4
        # modify v1[0,1] -> 0*4 + 1*2 + 1*8 -> 10
        # modify v2[1,2] -> -1*4 + 0*2 + 1*8 -> 4 

        # len 3 and k 2 -> 2 more modify -> 3-2 + 1 = 2
        # len 4 and k 2 -> 3 more modify -> 4-2 + 1 = 3
        
        # len 4 and k 4 -> 4-4 + 1 = 1 modification


        # prefix sum
        n = len(prices)
        profitSum = [0] * (n+1)
        priceSum = [0] * (n+1)
        for i in range(n):
            profitSum[i+1] = profitSum[i] + prices[i] * strategy[i]
            priceSum[i+1] = priceSum[i] + prices[i]
        
        res = profitSum[n]

        for i in range(k - 1, n):
            leftProfit = profitSum[i - k + 1]
            rightProfit = profitSum[n] - profitSum[i + 1]
            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            res = max(res, leftProfit + rightProfit + changeProfit)
        return res


        # TLE
        all_strategy = []
        for i in range(len(strategy) - k + 1):
            modified_strategy = strategy[:i] + [0] * (k//2) + [1] *(k//2) + strategy[i+k:]
            all_strategy.append(modified_strategy[:])
        
        all_strategy.append(strategy[:])
        
        res = -float('inf')
        for i in range(len(all_strategy)):
            curr = 0
            for j in range(len(prices)):
                curr += (prices[j] * all_strategy[i][j])
            res = max(res, curr)

        return res


        # 4 2 8
        #-1 0 1 -> 4

        # 4 2 8
        # 0 1 1 -> 10

        # 4 2 8
        #-1 0 1 -> 4