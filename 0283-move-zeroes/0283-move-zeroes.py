class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while 0 in nums:
            del nums[nums.index(0)]
            count += 1
        
        nums += [0] * count