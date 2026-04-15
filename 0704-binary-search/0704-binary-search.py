class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find upper bound and then check upperbound-1 == target
        # 1 2 3 4 5 -  4
        #     4

        left = 0
        right = len(nums)

        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        if left > 0 and nums[left-1] == target:
            return left - 1
        else:
            return -1



        # sorted nums

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1