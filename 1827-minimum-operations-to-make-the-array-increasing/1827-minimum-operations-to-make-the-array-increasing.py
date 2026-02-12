class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                target = nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
                res += target
        return res






        # strictly increasing
        # min_asc_number
        min_asc_number = float('-inf')
        for i, num in enumerate(nums):
            min_asc_number = max(num - i, min_asc_number)
        
        res = 0
        for i, num in enumerate(nums):
            target = min_asc_number + i
            res += (target - num) 

        return res
        # 1 5 2 4 1 -> min 4
        # 4 5 6 7 8
        # 4-1 = 3
        # 5-5 = 0
        # 6-2 = 4
        # 7-4 = 3
        # 8-1 = 7
