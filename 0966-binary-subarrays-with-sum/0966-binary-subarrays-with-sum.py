class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # sliding window
        def helper(target):
            if target < 0:
                return 0

            res = 0
            left = 0
            curr = 0
            for right in range(len(nums)):
                curr += nums[right]
                while curr > target:
                    curr -= nums[left]
                    left += 1
                res += right - left + 1
            return res
                
        return helper(goal) - helper(goal-1)



        # prefix sum
        freq = {0: 1}
        res,curr = 0, 0

        for num in nums:
            curr += num
            res += freq.get(curr - goal, 0)
            freq[curr] = freq.get(curr, 0) + 1
        return res





        
        
        
        # sliding window by size
        # TLE
        res = 0
        for size in range(1, len(nums)+1):
            # initial sliding window
            curr = sum(nums[:size]) 
            if curr == goal:
                res += 1
            for i in range(size, len(nums)): 
                curr += nums[i] - nums[i-size]
                if curr == goal:
                    res += 1
        return res

        
        # backtrack? no -> cuz of subarray, which means it needs to be contiguous

        # def backtrack(start, curr):
        #     print(curr)
        #     if sum(curr) == goal:
        #         return 1
        #     res = 0
        #     for i in range(start, len(nums)):
        #         curr.append(nums[i])
        #         res += backtrack(i+1, curr)
        #         curr.pop()

        #     return res

        # return backtrack(0, [])