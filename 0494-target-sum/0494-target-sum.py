class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        1 1 1 1 1  ==> 3
        - - - - - 

        every time I can choose + or -
        if at the end sum == target return 1
        """
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
        

