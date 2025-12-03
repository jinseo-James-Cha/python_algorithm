class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float('inf')] + nums + [float('inf')]

        n = len(nums)
        minimum_even_greater = 0
        minimum_odd_greater = 0

        for i in range(1, n-1, 2):
            if nums[i] >= min(nums[i-1], nums[i+1]):
                minimum_even_greater += nums[i] - min(nums[i-1], nums[i+1]) + 1
        
        for i in range(2, n-1, 2):
            if nums[i] >= min(nums[i-1], nums[i+1]):
                minimum_odd_greater += nums[i] - min(nums[i-1], nums[i+1]) + 1
        
        return min(minimum_even_greater, minimum_odd_greater)
        