class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [nums[0]]
        for num in nums:
            if num > subs[-1]:
                subs.append(num)
            else:
                i = 0
                while num > subs[i]:
                    i += 1
                subs[i] = num
        return len(subs)



        # maximum ?! or minimum ?! -> is it DP ?

        # 1. dp[i]
        
        # 2.recurrence relation -> a way to transition between states dp[5] and dp[7]
        # -> dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i

        # 3. base case
        
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)