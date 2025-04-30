class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         s = set(nums)
#         return not len(s) == len(nums)
        