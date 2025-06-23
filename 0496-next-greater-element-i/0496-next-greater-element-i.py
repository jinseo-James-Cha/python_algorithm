# v2 : can I optimize to O(nums1.length + nums2.length) 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2 make hashmap with all possible sets by stack
        hashmap = {}
        stack = []
        for n2 in nums2:
            while stack and n2 > stack[-1]:
                hashmap[stack.pop()] = n2
            stack.append(n2)       
        
        return [hashmap.get(i, -1) for i in nums1]
                
        


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         # all unique values
#         # all nums1 -> in nums2
#         # what is the next greater value..

#         # 4 -> 1, 3, 4 and 2 -> -1

#         # 2 4 3 1
        
#         # brute force O(N*M)
#         ans = []
#         for i in range(len(nums1)):
#             found = False
#             for j in range(len(nums2)):
#                 if found and nums1[i] < nums2[j]:
#                     ans.append(nums2[j])
#                     break
#                 if nums1[i] == nums2[j]:
#                     found = True
            
#             # if it didn't add
#             if len(ans) == i:
#                 ans.append(-1)
#         return ans
            
