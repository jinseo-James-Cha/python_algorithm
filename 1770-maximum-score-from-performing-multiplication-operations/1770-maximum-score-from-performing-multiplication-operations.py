class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        def dp(idx, left_idx):
            if idx == m:
                return 0
            
            if (idx, left_idx) not in memo:
                mult = multipliers[idx]
                # right idx = total size - 1 - (current_idx - chosen left idx)
                right = n - 1 - (idx - left_idx)  # 5 - (2-2) out of 5, left chosen 2 for 2 right is still 5

                # choosing max from the two options
                # max(left choose, right choose)
                memo[(idx, left_idx)] = max(mult * nums[left_idx] + dp(idx+1, left_idx+1), mult * nums[right] + dp(idx+1, left_idx))
            return memo[(idx, left_idx)]
        
        memo = {}
        return dp(0, 0)




        # this is wrong answer and here are the reasons
        # 1. memoization needs the whole states which are curr list, and i => need to put both and make it simple -> dont use list in the state
        # 2. I missed the best option because it choose by current situation by urr[0] * multipliers[i] > curr[-1] * multipliers[i]:
        # -> it is not choosing current's bigger value not optimization value in total
        n, m = len(nums), len(multipliers)
        
        def dp(curr, i):
            if i == len(multipliers):
                return 0

            if i not in memo:
                score = 0
                if curr[0] * multipliers[i] > curr[-1] * multipliers[i]:
                    score += curr[0] * multipliers[i] + dp(nums[1:], i+1)
                else:
                    score += curr[-1] *  multipliers[i] + dp(nums[:-1], i+1)
                memo[i] = score
            return memo[i]
        memo = {}
        return dp(nums, 0)























        # bottom up
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        # n >= m.
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]

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