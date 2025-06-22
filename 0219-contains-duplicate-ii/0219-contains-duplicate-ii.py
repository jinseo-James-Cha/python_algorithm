# v2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # keep saving latest index in hashmap and compare 
        # try to make O(N)
        hashmap = {}
        for index, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = index
                continue

            if abs(index - hashmap[num]) <= k:
                return True
            
            hashmap[num] = index

        return False


# v1: solved but I feel there is another way ..
# from collections import defaultdict
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         # 12 13 11 23 21 31
#         # i != j -> nums[i] == nums[j] and abs(0 - 3) <= 3
#         # loop find index pairs of nums[i] == nums[j]
#         # loop for abs(i - j) <= k ?
#         # 1 <= nums.length <= 10**5 -> no O(N**2)

#         # try with hashmap-defaultdict(list) because it can be multiple indexs
#         index_pairs = defaultdict(list)
#         for index, num in enumerate(nums):
#             index_pairs[num].append(index)

#         for key, value in index_pairs.items():
#             if len(value) < 2:
#                 continue

#             for i in range(len(value) - 1):
#                 for j in range(i + 1, len(value)):
#                     if abs(value[i] - value[j]) <= k:
#                         return True
        
#         return False
                

