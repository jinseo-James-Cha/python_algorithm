class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers solution 2
#         left = 0
#         for right in range(1, len(nums)):
#             if nums[left] == 0 and nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#             elif nums[left] != 0:
#                 left += 1
        
        # Two pointer solution
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


        # count = 0
        # while 0 in nums:
        #     del nums[nums.index(0)]
        #     count += 1
        
        # nums += [0] * count