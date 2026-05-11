class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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


        # backtracking
        def backtrack(start, curr_combination, remaining):
            if remaining < 0:
                return
            elif remaining == 0:
                res.append(curr_combination[:])
            
            for i in range(start, len(nums)):
                if target - nums[i] >= 0:
                    curr_combination.append(nums[i])
                    backtrack(i, curr_combination, remaining - nums[i])
                    curr_combination.pop()
            
        res = []
        backtrack(0, [], target)
        return len(res)