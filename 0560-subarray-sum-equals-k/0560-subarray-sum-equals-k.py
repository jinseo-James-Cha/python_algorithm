class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        # and nested loop all elements and sum
        # o(n^2) and o(n) for sum -> o(n^3) 

        # sum(i~j) = prefix_sum[j] - prefix_sum[i-1]
        # k = prefix_sum[j] - prefix_sum[i-1]
        # curr_total_sum - k = prev_sum
        # prev_sum in hashmap

        prev_sum = {0: 1}
        res = 0
        curr_total_sum = 0
        for num in nums:
            curr_total_sum += num
            if curr_total_sum - k in prev_sum:
                res += prev_sum[curr_total_sum - k]
            
            prev_sum[curr_total_sum] = prev_sum.get(curr_total_sum, 0) + 1
        return res

        # 1 1 1
        # 1
        # 11 -> 1, 1, 2
        # 1 1 1-> 1 1 2, + 1self + allsum

        # subarray sum = start - end
        # end = start - subarray sum
        # curr_total_sum = prev sum - k
        
        total = 0
        subarraySum_hashmap = { 0:1 }
        curr_total_sum = 0

        for num in nums:
            curr_total_sum += num
            if curr_total_sum - k in subarraySum_hashmap:
                total += subarraySum_hashmap[curr_total_sum - k]
            
            subarraySum_hashmap[curr_total_sum] = subarraySum_hashmap.get(curr_total_sum, 0) + 1
        return total
