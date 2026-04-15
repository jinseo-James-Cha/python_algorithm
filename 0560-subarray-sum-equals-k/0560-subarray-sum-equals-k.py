class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        subarray sum = k
        sum(i~j) = k
        prefix_sum(j) - prefix_sum(i-1) == k
        current_total - prev_prefix_sums == k
        current_total - k = prev_prefix_sum -> add the count of sum

        hash map to search o(1) for prev_prefix_sums

        # pseudocode
        initialize hashmap, curr_total_sum, count
        loop for all nums
            curr_total_sum add each num
            if curr_total_sum - k in hashmap:
                add how many times it has happened previously
            
            hashmap add 1 curr_total_sum which is prev now
        end loop
        return the count

        Time complexity: O(n)
        space complexity: o(n)
        """
        prev_prefix_sum = {0:1}
        curr_total_sum = 0
        total_count = 0
        for num in nums:
            curr_total_sum += num
            if curr_total_sum - k in prev_prefix_sum:
                total_count += prev_prefix_sum[curr_total_sum - k]
            
            prev_prefix_sum[curr_total_sum] = prev_prefix_sum.get(curr_total_sum, 0) + 1
        return total_count
