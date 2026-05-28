class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        sorted in ascending order -> binary search?
        but nums are rotated

        1 2 3 4 -> 3 4 1 2 -> 2 times left rotated
        return target is in nums with log n -> binary search but something different
        
        
        1 3 5 7 9 and 6
        L   M   R -> 5 < 6 we can move to right range cuz it is bigger than target always.
        if not gauranteed, we need to check where to move to.


        In each iteration, one half of the rotated array is always sorted. We determine which half is sorted, check if the target belongs to that range, and eliminate the other half. This allows us to perform a modified binary search in O(log n) time.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums and nums[left] == target else -1



