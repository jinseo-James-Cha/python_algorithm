# using hashmap -> O(N)

from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = defaultdict(int)
        for i, n2 in enumerate(nums2):
            hm[n2] = i

        for i, n1 in enumerate(nums1):
            nums1[i] = hm[n1]

        return nums1

# brute force - > O(N^2)
# class Solution:
#     def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         mapping = []
#         for n1 in nums1:
#             for i,n2 in enumerate(nums2):
#                 if n1 == n2:
#                     mapping.append(i)
#                     break
#         return mapping