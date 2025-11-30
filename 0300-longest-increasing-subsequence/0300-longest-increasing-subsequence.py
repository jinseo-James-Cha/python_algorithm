from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 10 9 2 5 3 7
        # 10
        # 9
        # 2
        # 2 5

        lis = [nums[0]]
        for i in range(1, len(nums)):
            if lis[-1] >= nums[i]:
                lis_idx = bisect_left(lis, nums[i])
                lis[lis_idx] = nums[i]
            else:
                lis.append(nums[i])
        return len(lis)












        # dp bottom up
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     current = 1
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             current = max(current, dp[j] + 1)
        #     dp[i] = current
        # return max(dp)

        # o(nlogn)
        subs = [nums[0]]
        for num in nums:
            if num > subs[-1]:
                subs.append(num)
            else:
                i = bisect_left(subs, num)
                subs[i] = num
        print(subs)
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