class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right: # left == right and return
            mid = (left + right) // 2

            if nums[mid] <= nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left