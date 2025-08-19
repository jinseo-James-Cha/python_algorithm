class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # bottom up
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]









        # Top down
        # def dp(i, left): # 0 0
        #     # Base case
        #     if i == m:
        #         return 0
            
        #     if (i, left) not in memo:
        #         mult = multipliers[i] # 3
        #         right = n - 1 - (i - left) # 3 - 1 - ( 0 - 0) = 2
                
        #         # Recurrence relation
        #         memo[(i, left)] =  max(mult * nums[left] + dp(i + 1, left + 1), 
        #                 mult * nums[right] + dp(i + 1, left))
        #     return memo[(i, left)]
                       
        # n, m = len(nums), len(multipliers)
        # memo = {}
        # return dp(0, 0)