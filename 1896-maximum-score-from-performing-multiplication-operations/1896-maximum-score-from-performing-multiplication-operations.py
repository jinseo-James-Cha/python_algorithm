class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Top down
        def dp(i, left): # 0 0
            # Base case
            if i == m:
                return 0
            
            if (i, left) not in memo:
                mult = multipliers[i] # 3
                right = n - 1 - (i - left) # 3 - 1 - ( 0 - 0) = 2
                
                # Recurrence relation
                memo[(i, left)] =  max(mult * nums[left] + dp(i + 1, left + 1), 
                        mult * nums[right] + dp(i + 1, left))
            return memo[(i, left)]
                       
        n, m = len(nums), len(multipliers)
        memo = {}
        return dp(0, 0)