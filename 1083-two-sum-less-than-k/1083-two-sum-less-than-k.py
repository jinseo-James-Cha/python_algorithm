class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # i < j? matters?
        # nums[i] + nums[j] = sum < k
        # I can do with O(n^2)..
        # let me start with brute force
        #
        res = -1 # max(res, X) if X < k
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < k:
                    res = max(res, nums[i] + nums[j])
        return res