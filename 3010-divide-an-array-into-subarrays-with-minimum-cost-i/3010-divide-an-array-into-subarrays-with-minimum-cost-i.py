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

        res = nums[0]
        copied = nums[1:]
        heapq.heapify(copied)
        for _ in range(2):
            res += heapq.heappop(copied)
        return res
        
        n = len(nums)
        # edge cases..
        if n == 3:
            return sum(nums)

        # the first element is always included
        # find two minimum values.
        res = nums[0]

        copied_nums = nums[1:]
        heapq.heapify(copied_nums)
        res += copied_nums[0] + copied_nums[1]
        return res


