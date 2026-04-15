class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        binary search
        """
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right - left) // 2
            
            left_val = nums[mid-1] if mid > 0 else float('-inf')
            right_val = nums[mid+1] if mid < n - 1 else float('-inf')
            if left_val < nums[mid] > right_val:
                return mid
            elif left_val > nums[mid]:
                right = mid - 1
            elif right_val > nums[mid]:
                left = mid + 1
        return -1


        """
        brute force -> o(n)
        check each element is greater than neighbors

        """
        n = len(nums)
        for i in range(n):
            left_val = nums[i-1] if i > 0 else float('-inf')
            right_val = nums[i+1] if i < n-1 else float('-inf')
            if left_val < nums[i] > right_val:
                return i
        return -1