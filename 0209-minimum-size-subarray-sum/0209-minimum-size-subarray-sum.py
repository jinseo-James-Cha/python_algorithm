class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        min_window = float('inf')
        total_sum = 0
        
        left = 0
        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                min_window = min(min_window, right - left + 1)
                total_sum -= nums[left]
                left += 1

        return min_window if min_window != float('inf') else 0
        
        
        # brute force -> TLE
        if sum(nums) < target:
            return 0
        
        res = 0
        if sum(nums) >= target:
            res = len(nums)
        for size in range(1, len(nums)):
            for i in range(len(nums)-size+1):
                if sum(nums[i:i+size]) >= target:
                    return size
        return res
