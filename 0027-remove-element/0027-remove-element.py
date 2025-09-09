class Solution:
    def removeElement(self, nums: List[int], val: int):
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = -1

        
        left = 0
        for right in range(len(nums)):
            if nums[right] != -1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left
