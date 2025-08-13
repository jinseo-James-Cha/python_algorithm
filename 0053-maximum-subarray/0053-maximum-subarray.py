class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # take?
        # or restart?
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            # compare nums[i] and current_sum which is current_sum + num[i]
            current_sum = max(nums[i], nums[i] + current_sum)
            max_sum = max(max_sum, current_sum)
        return max_sum