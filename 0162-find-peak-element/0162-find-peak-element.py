class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        brute force
        check each element is greater than neighbors

        """
        n = len(nums)
        for i in range(n):
            left_val = nums[i-1] if i > 0 else float('-inf')
            right_val = nums[i+1] if i < n-1 else float('-inf')
            if left_val < nums[i] > right_val:
                return i
        return -1