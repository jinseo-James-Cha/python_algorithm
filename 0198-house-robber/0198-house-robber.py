class Solution:
    def rob(self, nums: List[int]) -> int:
        # optimize from dp
        # i just need i - 1 and i - 2 to have answer
        # dp[-1] is the maximum profit..
        n = len(nums)
        if n == 1:
            return nums[0]

        prev_prev_profit = nums[0] # i - 2
        prev_profit = max(nums[0], nums[1]) # i - 1
        for i in range(2, len(nums)):
            current = max(prev_profit, prev_prev_profit + nums[i])

            prev_prev_profit = prev_profit
            prev_profit = current
        return prev_profit
            

        # dp
        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # return dp[-1]