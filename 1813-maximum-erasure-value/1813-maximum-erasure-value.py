class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window
        maximum_score = 0
        left = 0
        window = set()
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                left += 1
            
            window.add(nums[right])
            maximum_score = max(maximum_score, sum(window))
        return maximum_score

