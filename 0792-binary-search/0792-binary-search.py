# binary search O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # move mid to left
                right = mid - 1
            else: # move mid to right
                left = mid + 1

        return -1



        