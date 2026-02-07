class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
