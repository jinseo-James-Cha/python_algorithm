import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # O(n) / O(n)
        if len(nums) < 2:
            return 0
        
        # sort by radix sort
        def countingSortByDigit(nums, digit):
            buckets = [[] for _ in range(10)]
            for num in nums:
                bucket_idx = num // 10**digit % 10
                buckets[bucket_idx].append(num)
            return [x for bucket in buckets for x in bucket]

        max_num = max(nums)
        if max_num == 0:
            return 0
            
        digits = int(math.log10(max_num)) + 1
        sorted_list = nums[:]
        for digit in range(digits):
            sorted_list = countingSortByDigit(sorted_list, digit)
        
        maximum_gap = 0
        for i in range(1, len(sorted_list)):
            maximum_gap = max(maximum_gap, abs(sorted_list[i]-sorted_list[i-1]))
        return maximum_gap

