class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # v2 two pointers
        nums.sort()
        res = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < k:
                res = max(res, s)
                left += 1
            else:
                right -= 1
        return res



        # i < j? matters? no
        # nums[i] + nums[j] = sum < k
        # I can do with O(n^2)..
        # let me start with brute force
        #
        # res = -1 # max(res, X) if X < k
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < k:
        #             res = max(res, nums[i] + nums[j])
        # return res