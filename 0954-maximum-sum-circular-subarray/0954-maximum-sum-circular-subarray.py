class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max_sum = nums[0]
        total_max_sum = nums[0]

        curr_min_sum = nums[0]
        total_min_sum = nums[0]

        total_sum = nums[0]

        for i in range(1, len(nums)):
            curr_max_sum = max(nums[i], curr_max_sum + nums[i])
            total_max_sum = max(total_max_sum, curr_max_sum)

            curr_min_sum = min(nums[i], curr_min_sum + nums[i])
            total_min_sum = min(total_min_sum, curr_min_sum)

            total_sum += nums[i]
        
        print(curr_max_sum, total_max_sum, curr_min_sum, total_min_sum)
        
        # if all nums are negative -3 -2 -1
        if total_sum - total_min_sum == 0:
            return total_max_sum
        
        return max(total_max_sum, total_sum - total_min_sum)