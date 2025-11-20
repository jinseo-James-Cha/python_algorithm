class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peek => greater than neighbors
        # find a peek and return its "index"
        # if multiple, return any of them
        # O(log n) -> binary search
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    def binarySearch(self, nums, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] > nums[mid+1]:
            return self.binarySearch(nums, left, mid)
        return self.binarySearch(nums, mid+1, right)