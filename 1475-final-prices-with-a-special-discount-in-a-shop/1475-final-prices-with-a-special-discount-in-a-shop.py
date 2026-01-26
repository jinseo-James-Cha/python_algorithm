from collections import deque
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # special discount
        # if you buy "i"th item, discount prices[j] ==> minimum index j > i and prices[j] <= prices[i]



        """
        8 4 6 2 3
        4 2 4 2 3


        stack [8]
        8 > 4
        pop
        answer[4]
        
        stack [4]
        4 < 6
        push
        
        stack [4, 6]
        6 > 2
        pop
        [4]
        4 > 2
        pop
        [4, 2]
        stack[4, 2, 4]
        push 2
        
        stack[2]
        stack[2,3]

        [4,2,4] + [2,3]
        [1, 2, 3, 4, 5]

        8 4 6 5
        [4]

        [4, 6]
        5

        [1 4] 
        monotonic stack ? no..?



        8 4 6 2 3
        4 2 4 2 3

        """
        # monotonic stack
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
