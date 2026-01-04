class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up optimize
        if len(nums) == 1:
            return nums[0]
        
        two_back = nums[0]
        one_back = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = one_back
            one_back = max(two_back + nums[i], temp)
            two_back = temp
        return one_back

        # bottom up
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums)-1]


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