class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # maximum ?! or minimum ?! -> is it DP ?

        # 1. dp[i]
        
        # 2.recurrence relation -> a way to transition between states dp[5] and dp[7]
        # -> dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i

        # 3. base case
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)