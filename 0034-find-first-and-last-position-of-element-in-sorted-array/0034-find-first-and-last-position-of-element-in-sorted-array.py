# v3: gpt answer O(log(N))
# more make sense to me
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound_binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:   
                    right = mid 
            return left if left < len(nums) and nums[left] == target else -1

        # rightmost occurrence of the target
        def upper_bound_binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1 if left > 0 and nums[left - 1] == target else -1

        lower_bound = lower_bound_binary_search(nums, target)
        upper_bound = upper_bound_binary_search(nums, target)
        return [lower_bound, upper_bound]
# v2: o(log(n))
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # will be greater than target
#         # will be less than target
#         # will be equal to target

#         # leftmost occurrence of the target
#         # when mid value is equal to the target.. two possibilities
#         # 1. this is the lower bound
#         # 2. this is not lower, the lower bound is further to the left
#         def lower_bound_binary_search(nums: List[int], target: int) -> int:
#             left, right = 0, len(nums) - 1
#             while left < right:
#                 mid = (left + right) // 2
#                 if nums[mid] > target:
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             return right if nums and nums[right] == target else -1
        
#         # rightmost occurrence of the target
#         def upper_bound_binary_search(nums: List[int], target: int) -> int:
#             left, right = 0, len(nums) - 1
#             while left < right:
#                 mid = (left + right) // 2 + 1
#                 if nums[mid] > target:
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     left = mid
#             return left if nums and nums[right] == target else -1

#         lower_bound = lower_bound_binary_search(nums, target)
#         upper_bound = upper_bound_binary_search(nums, target)
#         return [lower_bound, upper_bound]


# sorted integers in ascending order.
# find target
# binary search question

# My solution is O(n), but 100% beat..?!
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         res = [-1, -1]

#         # do binary search first
#         left = 0
#         right = len(nums) - 1
#         mid = (left + right) // 2
#         target_index = -1
#         while left <= right:
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 target_index = mid
#                 break
#             mid = (left + right) // 2
        
#         if target_index == -1:
#             return res

#         # find lower bound with left ~ mid-1
#         while left <= mid:
#             if nums[left] == target:
#                 res[0] = left
#                 break
#             left += 1
        
#         # find uppur bound with mid ~ right
#         while mid <= right:
#             if nums[mid] == target:
#                 res[1] = mid
#             mid += 1
    
#         return res
        