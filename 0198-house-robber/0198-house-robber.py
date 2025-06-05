class Solution:
    def rob(self, nums: List[int]) -> int:
        # odd and even difference? no they can rob 1st , 4th house
        # even_houses = sum(nums[::2])
        # odd_houses = sum(nums[1::2])

        # then choose every single time for 1,2 and step by 2?
        

        # no.. it uses DP
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]