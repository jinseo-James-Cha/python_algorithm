# second solution
# create another integer list include lower and upper and linear iterator
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        new_nums = [lower - 1] + nums + [upper + 1]
        for i in range(len(new_nums) - 1):
            if new_nums[i] < new_nums[i+1] - 1:
                res.append([new_nums[i]+1,  new_nums[i+1]-1])
        return res

# class Solution:
#     def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
#         # nums = sorted unique integer
#         # x is missing if lower < x < upper and not in nums
#         # return shortest sorted list of ranges that exactly covers all the missing numbers

#         # All the values of nums are unique.
#         # why is this given.. something better with unique nums..?

#         res = []

#         if len(nums) == 0:
#             return [[lower, upper]]

#         for i, n in enumerate(nums):
#             # first i needs to compare with lower
#             if i == 0:
#                 if lower + 1 <= nums[i]:
#                     res.append([lower, nums[0]-1])
#             # last i needs to compare with upper
            
#             if i == len(nums) - 1:
#                 if nums[i] + 1 <= upper:
#                     res.append([nums[i] + 1, upper])
#             # compare i - i+1
#             else:
#                 if n + 1 < nums[i+1]:
#                     res.append([n+1, nums[i+1] - 1])

#         return res
