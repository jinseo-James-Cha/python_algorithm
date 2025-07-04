class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # uhm two pointers
        # left moves if right is less than left
        maximum = -1
        left = 0
        for right in range(1, len(nums)):
            if nums[right] > nums[left]:
                maximum = max(maximum, nums[right] - nums[left])
            
            if nums[right] < nums[left]:
                left = right
        
        return maximum