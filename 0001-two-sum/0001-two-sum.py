# uhm.. I can use inward traversal two pointers if its sorted list.
# You may assume that each input would have exactly one solution,
# not use the same element twice.

# v2: hash table solution
# O(N) because hash table lookup time is O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        res = []
        for i, num in enumerate(nums):
            if target - num in hashmap:
                res = [hashmap[target - num], i]
                break
            hashmap[num] = i
        return res










        # d = {}
        
        # for i,n in enumerate(nums):
        #     t = target - n
        #     if t in d:
        #         return [i, d[t]]
        #     d[n] = i
        # return []



# brute force O(N^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+ nums[j] == target:
#                     return [i, j]
#         return []            
            