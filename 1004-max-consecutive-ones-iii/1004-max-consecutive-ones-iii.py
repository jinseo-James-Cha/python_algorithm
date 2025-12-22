class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # [1,1,1,0,0,0,1,1,1,1,0] and k = 2
        # [1,1,1,0,0,1,1,1,1,1,1] maxinum length = 6
        # make temp k and move one by one with sliding window
        # multiple 1 and k much 0 in window and length for maximym


        left = 0
        curr = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans


