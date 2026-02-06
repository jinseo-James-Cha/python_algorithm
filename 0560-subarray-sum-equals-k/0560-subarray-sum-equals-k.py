from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1
        curr_prefix_sum = 0
        for num in nums:
            curr_prefix_sum += num
            
            if curr_prefix_sum - k in prefix_sum_map:
                count += prefix_sum_map[curr_prefix_sum - k]

            prefix_sum_map[curr_prefix_sum] += 1
        return count


# using prefix_sum algorithm 
# O(n^2) 
# 1 <= nums.length <= 2 * 10^4 -> TLE
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0
        
#         prefix_sum = [0] # for just prefix index itself
#         for i in range(len(nums)):
#             prefix_sum.append(prefix_sum[-1] + nums[i])
        
#         for j in range(1, len(nums) + 1):
#             for i in range(1, j + 1):
#                 if prefix_sum[j] - prefix_sum[i - 1] == k:
#                     res += 1
#         return res            