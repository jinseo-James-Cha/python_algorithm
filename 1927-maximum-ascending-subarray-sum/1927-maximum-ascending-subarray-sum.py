class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = prevNum = cycleSum = nums[0]  # initial with the first element 1 <= nums.length <= 100
        
        for i in range(1, len(nums)):
            if nums[i] > prevNum:
                cycleSum += nums[i]
            else:
                cycleSum = nums[i]
            maxSum = max(maxSum, cycleSum)
            prevNum = nums[i]
        return maxSum