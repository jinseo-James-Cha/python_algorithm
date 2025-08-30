class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maximum agv means maximum sum
        # so return / 4 
        
        LESS_THAN = 10**-5
        n = len(nums)

        if n < 5:
            return sum(nums) / n

        current = sum(nums[:k])
        max_sum = current
        for i in range(k, n):
            current = current - nums[i-k] + nums[i]
            max_sum = max(max_sum, current)
        return max_sum / k