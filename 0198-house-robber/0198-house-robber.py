class Solution:
    def rob(self, nums: List[int]) -> int:
        # maximum amount I can rob ?! -> DP question?!
        # opitimized bottom-up
        # I just need the prev, and the prev prev until the last !
        if len(nums) == 1:
            return nums[0]
        
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = max(prev, prev_prev + nums[i])
            prev_prev = prev
            prev = current
        return prev


        # bottom-up / tabulation
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        # return dp[-1]



        # top-down / memoization
        # def calculate_rob(i):
        #     if i == 0:
        #         return nums[0]
        #     elif i == 1:
        #         return max(nums[0], nums[1])
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(calculate_rob(i-2) + nums[i], calculate_rob(i-1))
        #     return memo[i]
        # memo = {}
        # return calculate_rob(len(nums)-1)