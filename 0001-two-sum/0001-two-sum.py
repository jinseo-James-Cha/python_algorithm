# uhm.. I can use inward traversal two pointers if its sorted list.
# You may assume that each input would have exactly one solution,
# not use the same element twice.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        # no dup
        for i,n in enumerate(nums):
            t = target - n
            if t in d and i != d[t]:
                return [i, d[t]]



# brute force O(N^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+ nums[j] == target:
#                     return [i, j]
#         return []            
            