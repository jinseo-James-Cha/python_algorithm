class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # two pointer or sliding window feeling
        # but space is different
        # If you have figured out the O(n) solution, 
        # try coding another solution using "the divide and conquer" approach, which is more subtle.

        # two pointer !!
        # but I don't get when moves pointer
        # where to put right pointer

        # no... I am wrong
        res = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            
            total += num
            res = max(total, res)
        return res
            

            