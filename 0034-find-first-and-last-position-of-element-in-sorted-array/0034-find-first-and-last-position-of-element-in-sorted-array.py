# sorted integers in ascending order.
# find target
# binary search question
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        # do binary search first
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        target_index = -1
        while left <= right:
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                target_index = mid
                break
            mid = (left + right) // 2
        
        if target_index == -1:
            return res

        # find lower bound with left ~ mid-1
        while left <= mid:
            if nums[left] == target:
                res[0] = left
                break
            left += 1
        
        # find uppur bound with mid ~ right
        while mid <= right:
            if nums[mid] == target:
                res[1] = mid
            mid += 1
    
        return res
        