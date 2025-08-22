class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # circular nums
        # maximum subarray

        def maxKadane(numbers):
            current = 0 
            max_sum = float(-inf)
            for num in numbers:
                current = max(num, current+num)
                max_sum = max(max_sum, current)

            return max_sum
        
        def minKadane(numbers):
            current = 0
            min_sum = float(inf)
            for num in numbers:
                current = min(num, current+num)
                min_sum = min(min_sum, current)
            return min_sum

        n = len(nums)
        max_kadane_sum = maxKadane(nums)

        total_sum = sum(nums)
        min_kadane_sum = minKadane(nums)
        max_circular = total_sum - min_kadane_sum
        if max_circular == 0:
            return max_kadane_sum
        
        return max(max_kadane_sum, max_circular)