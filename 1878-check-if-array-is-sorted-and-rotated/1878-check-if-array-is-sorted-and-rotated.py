# v1 : O(n)
class Solution:
    def check(self, nums: List[int]) -> bool:
        # count reversed pair
        # if more than 1 -> return False
        reversedPair = 0
        for i in range(len(nums) - 1):
            # reversed, desc order
            if nums[i] > nums[i+1]:
                reversedPair += 1

            if reversedPair > 1:
                return False
        
        if nums[0] < nums[len(nums)-1]:
            reversedPair += 1
        return reversedPair <= 1

# O(n^2)
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         # true -> ASC order and rotate some number of positions
#         # binary search to find x > x + 1 ??!?!?


#         # B[i] == A[(i+x) % A.length]
#         # 1 2 3 4 5 / 0~4
#         # 0:5 + 0:0 -> 12345 + ""
#         # 1:5 + 0:1 -> 2345 + 1
#         A = sorted(nums)
#         for i in range(len(nums)):
#             B = nums[i:] + nums[:i] 
#             if B == A:
#                 return True
#         return False
