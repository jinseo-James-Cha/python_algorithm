class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sub = max_sub = nums[0]
        for num in nums[1:]:
            curr_sub = max(num, curr_sub + num)
            max_sub = max(curr_sub, max_sub)
        return max_sub