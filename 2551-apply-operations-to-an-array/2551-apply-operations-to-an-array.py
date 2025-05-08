class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                continue
            elif nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # Two pointer
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != 0 and nums[right] == 0:
                left = right
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
        