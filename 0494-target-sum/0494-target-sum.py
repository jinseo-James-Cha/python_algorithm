class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        1 1 1 1 1  ==> 3
        - - - - - 

        every time I can choose + or -
        if at the end sum == target return 1
        """

        # bottom up
        total = sum(nums)

        if abs(target) > total:
            return 0

        offset = total
        n = len(nums)

        dp = [[0] * (2 * total + 1) for _ in range(n + 1)]
        dp[0][offset] = 1  # sum = 0

        for i in range(1, n + 1):
            for s in range(2 * total + 1):
                if dp[i-1][s] != 0:
                    dp[i][s + nums[i-1]] += dp[i-1][s]
                    dp[i][s - nums[i-1]] += dp[i-1][s]

        return dp[n][target + offset]




        # top down
        def dp(i,curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            
            # can choose two cases
            if (i, curr_sum) not in memo:
                add = dp(i + 1, curr_sum + nums[i])
                subtract = dp(i + 1, curr_sum - nums[i])

                memo[(i, curr_sum)] = add + subtract
            return memo[(i, curr_sum)]
        
        memo = {}
        return dp(0, 0)
        

