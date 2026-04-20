class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        subarray sum
        sum(i~j) == k
        prefix_sum[j] - prefix_sum[i-1] == k
        prefix_sum[j] - k == prefix_sum[i-1]
        1 2 3 = 3
        
        1:0
        3 - 2 in 
        i - prev[total - k]
        3:1

        curr_sum_total_j - k in prev_subarray_sum: i -> 
        j - i -> the length and update by maximum

        """
        prev_subarray_sum = {} # key: i
        curr_sum_total = 0
        maximum_size = 0
        for i, num in enumerate(nums):
            curr_sum_total += num

            if curr_sum_total == k:
                maximum_size = i + 1

            if curr_sum_total - k in prev_subarray_sum:
                maximum_size = max(maximum_size, i - prev_subarray_sum[curr_sum_total - k])
            
            if curr_sum_total not in prev_subarray_sum:
                prev_subarray_sum[curr_sum_total] = i

        return maximum_size