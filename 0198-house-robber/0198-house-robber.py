class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

        # top down
        # def dp(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
            
        #     if i in memo:
        #         return memo[i]

        #     memo[i] = max(dp(i-2) + nums[i], dp(i-1))
        #     return memo[i]
        
        # memo = {}
        # return dp(len(nums)-1)