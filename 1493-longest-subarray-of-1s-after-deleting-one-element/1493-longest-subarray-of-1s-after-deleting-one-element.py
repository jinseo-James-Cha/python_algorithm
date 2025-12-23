class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # one element skip(delete)..
        # include one 0 element and return len - 1
        # sliding window

        # [0,1,1,1,0,1,1,0,1]
        #    L
        #          R
        left = 0
        zero_count = 0
        max_size = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_size = max(max_size, right - left + 1)
                
        return max_size - 1