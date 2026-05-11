class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp - bottom up
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]
        return dp[target]

        # dp - top down
        def dp(remaining):
            if remaining < 0:
                return 0
            elif remaining == 0:
                return 1
            
            if remaining not in memo:
                total = 0
                for i in range(len(nums)):
                    if remaining - nums[i] >= 0:
                        total += dp(remaining - nums[i])
                memo[remaining] = total
            return memo[remaining]

        memo = {}
        return dp(target)


        # backtracking -> NOT WORKING -> it didn't have prev nums in the combinations..
        # def backtrack(start, curr_combination, remaining):
        #     if remaining < 0:
        #         return
        #     elif remaining == 0:
        #         res.append(curr_combination[:])
        #         return
            
        #     for i in range(start, len(nums)):
        #         if remaining - nums[i] >= 0:
        #             curr_combination.append(nums[i])
        #             backtrack(i, curr_combination, remaining - nums[i])
        #             curr_combination.pop()
            
        # res = []
        # backtrack(0, [], target)
        # return len(res)