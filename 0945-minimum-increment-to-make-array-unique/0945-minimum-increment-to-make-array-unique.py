class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        freq_count = [0] * (max_val + n)
        for num in nums:
            freq_count[num] += 1
        
        for i in range(len(freq_count)):
            if freq_count[i] <= 1:
                continue
            
            duplicates = freq_count[i] - 1
            freq_count[i+1] += duplicates
            freq_count[i] = 1
            min_increments += duplicates
        return min_increments



        # 1 2 2
        # 1 2 3 -> 1

        # 3 2 1 2 1 7
        # 1 1 2 2 3 7
        # 1 2 3 4 5 7 -> 1+1+2+2
        # 1 1->4 2 2->5 3 7

        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                target = nums[i-1] + 1
                res += target - nums[i]
                nums[i] = target
        return res