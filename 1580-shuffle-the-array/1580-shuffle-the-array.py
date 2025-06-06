
# better
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

# not bad mine
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         res = []
#         left = 0
#         right = n
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 res.append(nums[left])
#                 left += 1
#             else:
#                 res.append(nums[right])
#                 right += 1
#         return res
