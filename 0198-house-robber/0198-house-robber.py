class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-2) + nums[i], dp(i-1))
            return memo[i]
        
        memo = {}
        return dp(len(nums)-1)