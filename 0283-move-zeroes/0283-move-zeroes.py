class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1