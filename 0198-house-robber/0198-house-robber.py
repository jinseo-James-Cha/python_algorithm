class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        either take this house or skip this for the next house?
        state: house index
        """
        # bottom up
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

        # top down
        def dp(i):
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        memo = {}
        return dp(len(nums)-1)
