import heapq
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # cost = the first element of an array

        # divide nums into 3 disjoint contiguous subarrays
        # return the minimum possible sum of the cost..

        # 1 2 3 12
        # 1 / 2 / 3 12 -> 6
        # nums 1 ~ 50...

        """
        len 4
        need to divide by 3...  1 1 2..

        10 3 1 1
        10 3 / 1 / 1 

        """
        n = len(nums)
        # edge cases..
        if n == 3:
            return sum(nums)

        # set maximum value
        a, b = 51, 51
        # a <= b
        for i in range(1, n):
            if nums[i] < a:
                b = a
                a = nums[i]
            elif nums[i] < b:
                b = nums[i]
            
            # exit case
            if a == 1 and b == 1:
                break
        return nums[0] + a + b




        # Heapq
        n = len(nums)
        # edge cases..
        if n == 3:
            return sum(nums)

        res = nums[0]
        copied = nums[1:]
        heapq.heapify(copied)
        for _ in range(2):
            res += heapq.heappop(copied)
        return res

