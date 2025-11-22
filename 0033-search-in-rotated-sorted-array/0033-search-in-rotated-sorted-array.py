class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        # using Binary search, but its partially not sorted !?
        # like 12345 -> 45123
        # one index has bigger than next index
        # two parts of array 
        
        # need to check non-ascending order
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # if nums[left:mid] is proper asceding order list
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