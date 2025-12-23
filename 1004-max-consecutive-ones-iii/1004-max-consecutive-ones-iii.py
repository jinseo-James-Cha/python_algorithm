class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window
        left = 0
        curr_len = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr_len += 1
            
            while curr_len > k:
                if nums[left] == 0:
                    curr_len -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        return max_len