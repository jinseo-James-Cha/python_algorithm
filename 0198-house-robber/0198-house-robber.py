class Solution:
    def rob(self, nums: List[int]) -> int:
        # maximum amount I can rob ?! -> DP question?!
        # top-down / memoization
        def calculate_rob(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(calculate_rob(i-2) + nums[i], calculate_rob(i-1))
            return memo[i]
        memo = {}
        return calculate_rob(len(nums)-1)
        

        # bottom-up / tabulation